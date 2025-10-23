# 🎓 LangGraph Complete Training Guide
## From Zero to AI Agent Mastery

---

## 📚 Table of Contents

1. [**Introduction & Setup**](#1-introduction--setup)
2. [**Core Concepts**](#2-core-concepts)
3. [**Building Your First Graph**](#3-building-your-first-graph)
4. [**Messages & Conversations**](#4-messages--conversations)
5. [**Tool Calling**](#5-tool-calling)
6. [**State Management**](#6-state-management)
7. [**Complete Agents**](#7-complete-agents)
8. [**ReACT Pattern**](#8-react-pattern)
9. [**Memory & Persistence**](#9-memory--persistence)
10. [**Real-World Project**](#10-real-world-project)
11. [**Advanced Topics**](#11-advanced-topics)

---

## 1. Introduction & Setup

### What is LangGraph? 🤔
**Simple Explanation:** Think of LangGraph as a recipe book for AI agents. Just like a recipe has steps (chop onions → heat oil → add ingredients), LangGraph lets you create AI workflows with clear steps that can make decisions and use tools.

**Technical Definition:** LangGraph is a framework for building stateful, multi-step applications with Large Language Models (LLMs).

### Why Use LangGraph? 🎯
- **Decision Making:** Your AI can choose different paths based on what it learns
- **Tool Usage:** Your AI can perform actions (calculations, API calls, etc.)
- **Memory:** Your AI remembers previous conversations
- **Complex Reasoning:** Handle multi-step problems that require thinking and acting

### Prerequisites ✅
- Basic Python knowledge
- OpenAI API key
- Understanding of AI/LLM concepts

### Environment Setup 🛠️

#### Step 1: Create Virtual Environment
```bash
# Create virtual environment
python3.12 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

#### Step 2: Install Dependencies
Create `requirements.txt`:
```txt
langchain-core
langgraph
langgraph-checkpoint
langgraph-prebuilt
jupyter
ipykernel
langchain-openai
pandas
pydantic
pydantic_core
python-dotenv
```

Install packages:
```bash
pip install -r requirements.txt
```

#### Step 3: OpenAI Configuration
Create `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

#### Step 4: Test Setup
```python
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize model
model = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o",
    max_tokens=512,
    temperature=0.1,
)

# Test connection
msg = HumanMessage(content="Hi, how are you?")
response = model.invoke([msg])
print(response.content)
```

**Expected Output:**
```
Hi! I'm doing well, thank you for asking. How can I help you today?
```

---

## 2. Core Concepts

### Understanding Graphs 📊

**Simple Explanation:** A graph is like a flowchart where:
- **Boxes (Nodes)** = Functions that do something
- **Arrows (Edges)** = Show what happens next
- **Data (State)** = Information that flows through the boxes

**Visual Representation:**
```
Input Data → [Process A] → [Decision Point] → [Process B] or [Process C] → Output
```

### Key Components 🧩

#### 1. State
**What it is:** The data that flows through your workflow
**Simple Example:** Like a shopping cart that gets filled as you go through a store

```python
from typing_extensions import TypedDict

class State(TypedDict):
    graph_state: str  # This is our "shopping cart"
```

#### 2. Nodes
**What they are:** Functions that process and modify the state
**Simple Example:** Like workers in a factory assembly line

```python
def node_1(state):
    print("Node 1 working...")
    return {"graph_state": state["graph_state"] + " will"}

def node_2(state):
    print("Node 2 working...")
    return {"graph_state": state["graph_state"] + " go surfing"}
```

#### 3. Edges
**What they are:** Connections that determine the flow between nodes
**Simple Example:** Like road signs that tell you which way to go

```python
# Simple edge: always go from A to B
builder.add_edge(START, "node_1")

# Conditional edge: choose based on conditions
builder.add_conditional_edges("node_1", decide_mood_node)
```

---

## 3. Building Your First Graph

### Project: Activity Selector 🎯

**Goal:** Build a simple AI that decides what activity someone will do based on a random "mood".

### Step-by-Step Implementation

#### Step 1: Define the State
```python
from typing_extensions import TypedDict

class State(TypedDict):
    graph_state: str
```

**Explanation:** This defines what data our graph will work with. In this case, just a string that gets built up as we go.

#### Step 2: Create the Nodes
```python
def node_1(state):
    print("Node 1")
    return {"graph_state": state["graph_state"] + " will"}

def node_2(state):
    print("Node 2")
    return {"graph_state": state["graph_state"] + " go surfing"}

def node_3(state):
    print("Node 3")
    return {"graph_state": state["graph_state"] + " go rock climbing"}
```

**Explanation:** Each node takes the current state, does something with it, and returns an updated state.

#### Step 3: Create Decision Logic
```python
import random
from typing import Literal

def decide_mood_node(state) -> Literal["node_2", "node_3"]:
    user_input = state["graph_state"]
    if random.random() < 0.5:
        return "node_2"
    return "node_3"
```

**Explanation:** This function looks at the current state and decides which node to run next. It's like a coin flip - 50% chance of each option.

#### Step 4: Build the Graph
```python
from langgraph.graph import StateGraph, START, END

# Create the graph builder
builder = StateGraph(State)

# Add nodes
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# Add edges
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood_node)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

# Compile the graph
graph = builder.compile()
```

**Explanation:** This connects everything together. START always goes to node_1, then node_1 decides between node_2 or node_3, and both of those go to END.

#### Step 5: Run the Graph
```python
# Run the graph
result = graph.invoke({"graph_state": "Vikkas will"})
print(result)
```

**Expected Output:**
```
Node 1
Node 2
{'graph_state': 'Vikkas will go surfing'}
```

**Or:**
```
Node 1
Node 3
{'graph_state': 'Vikkas will go rock climbing'}
```

### Visualizing the Graph
```python
from IPython.display import Image, display

# Display the graph structure
display(Image(graph.get_graph().draw_mermaid_png()))
```

**What you'll see:** A flowchart showing START → node_1 → (decision) → node_2 or node_3 → END

---

## 4. Messages & Conversations

### Understanding Messages 💬

**Simple Explanation:** Messages are like text messages between you and the AI. They keep track of the conversation history so the AI remembers what you talked about.

### Message Types 📝

#### 1. HumanMessage
**What it is:** Messages from the user
```python
from langchain_core.messages import HumanMessage

user_msg = HumanMessage(content="Hello, how are you?")
```

#### 2. AIMessage
**What it is:** Responses from the AI
```python
from langchain_core.messages import AIMessage

ai_msg = AIMessage(content="I'm doing well, thank you!")
```

#### 3. SystemMessage
**What it is:** Instructions for the AI
```python
from langchain_core.messages import SystemMessage

system_msg = SystemMessage(content="You are a helpful assistant.")
```

#### 4. ToolMessage
**What it is:** Results from tool executions
```python
from langchain_core.messages import ToolMessage

tool_msg = ToolMessage(content="24", tool_call_id="123")
```

### Building Conversations 🔄

#### Step 1: Create Message List
```python
from langchain_core.messages import HumanMessage, AIMessage

messages = [HumanMessage(content="There are 600+ CRR related regulations")]
messages.append(AIMessage(content="Thanks for the information, that is great to know, would you like me to elaborate on any of these"))
messages.append(HumanMessage(content="Give me details of 1 regulation which applies to TechBank International"))
```

#### Step 2: Process with LLM
```python
# Create a new model instance
model2 = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o",
    max_tokens=512,
    temperature=0.1,
)

# Send the conversation to the model
result = model2.invoke(messages)
print(result.content)
```

**Expected Output:**
```
Here's a detailed overview of one key CRR regulation that applies to TechBank International:

## CRR Article 92 — Own Funds Requirements
**Regulation:** EU Regulation 575/2013, Article 92
**Applies to:** All credit institutions including TechBank International plc and TechBank International Bank plc

### Key Requirements:
**Minimum Capital Ratios:**
- Common Equity Tier 1 (CET1) ratio: minimum 4.5%
- Tier 1 capital ratio: minimum 6%
- Total capital ratio: minimum 8%

### How it applies to TechBank International:
**Current Status (as of recent reports):**
- TechBank International maintains CET1 ratios well above minimum requirements
- Typically operates with CET1 ratios around 13–15%
- Must report these ratios quarterly to regulators

**Practical Impact:**
- Determines how much risk-weighted assets TechBank International can hold
- Influences lending capacity and business strategy
- Affects dividend distribution capabilities
- Triggers regulatory intervention if breached

**Compliance Mechanisms:**
- Regular stress testing
- Capital planning processes
- Risk appetite frameworks
- Monthly monitoring and reporting

This regulation is fundamental as it directly impacts TechBank International's ability to operate, lend, and distribute profits to shareholders.

"Would you like me to elaborate on any specific aspect of this regulation or discuss another CRR article?"
```

### Understanding Message Flow 🔄

**Visual Flow:**
```
User Message → Graph → LLM → AI Response → Add to State → Continue
```

**Key Point:** Messages accumulate in the state, so the AI always has the full conversation context.

---

## 5. Tool Calling

### What are Tools? 🛠️

**Simple Explanation:** Tools are like giving your AI superpowers. Instead of just talking, it can:
- Do calculations
- Look up information
- Call APIs
- Execute functions

### How Tool Calling Works 🔧

**Process:**
1. User asks a question
2. AI decides if it needs a tool
3. AI calls the tool with parameters
4. Tool executes and returns result
5. AI uses result to answer the user

### Creating Your First Tool 🎯

#### Step 1: Define the Tool Function
```python
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers and returns an integer
    
    Args:
        a: first integer
        b: second integer
    """
    return a * b
```

**Important:** The docstring is crucial! The AI reads this to understand when and how to use the tool.

#### Step 2: Bind Tools to Model
```python
# Create model with tools
model2_with_tools = model2.bind_tools([multiply])
```

#### Step 3: Test Tool Calling
```python
# Ask a question that requires the tool
result = model2_with_tools.invoke([HumanMessage(content="What is 4 times 6?")])

print("AI Response:", result.content)
print("Tool Calls:", result.tool_calls)
```

**Expected Output:**
```
AI Response: I'll calculate 4 times 6 for you.
Tool Calls: [{'name': 'multiply', 'args': {'a': 4, 'b': 6}, 'id': 'call_123'}]
```

**Explanation:** The AI recognized it needs to use the multiply tool and generated a tool call with the correct parameters.

### Understanding Tool Call Structure 📊

```python
# Inspect the tool call details
tool_call = result.tool_calls[0]
print("Function name:", tool_call['name'])
print("Arguments:", tool_call['args'])
print("Call ID:", tool_call['id'])
```

**Expected Output:**
```
Function name: multiply
Arguments: {'a': 4, 'b': 6}
Call ID: call_123
```

---

## 6. State Management

### The Problem with State 🔄

**Issue:** By default, when a node returns state, it replaces the old value.

```python
# This would REPLACE messages (BAD!)
class MessagesState(TypedDict):
    messages: List[AnyMessage]  # This loses previous messages!
```

**Problem:** If node 1 adds a message and node 2 adds another, you'd lose node 1's message!

### The Solution: Reducers 🧩

**Simple Explanation:** Reducers are like smart merge functions that combine old and new data instead of replacing it.

#### Using the add_messages Reducer
```python
from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
```

**Explanation:** This tells LangGraph to use the `add_messages` function to merge old and new messages.

#### How add_messages Works
```python
from langchain_core.messages import HumanMessage, AIMessage

# Initial messages
initial_messages = [
    HumanMessage(content="Hi how are you"),
    AIMessage(content="I am good, thank you")
]

# New message
new_message = [HumanMessage(content="What is the role of PRA in banking")]

# Merge them
combined = add_messages(initial_messages, new_message)
print(combined)
```

**Expected Output:**
```
[HumanMessage("Hi how are you"),
 AIMessage("I am good, thank you"),
 HumanMessage("What is the role of PRA in banking")]
```

**Key Point:** Messages accumulate instead of being replaced!

---

## 7. Complete Agents

### Building a Complete Agent 🤖

**Goal:** Create an agent that can receive questions, decide which tools to use, execute them, and return results.

### Key Components

#### 1. ToolNode
**What it is:** A pre-built LangGraph component that automatically executes tool calls
**Benefits:** Handles errors, returns results as ToolMessages, saves you from manual implementation

#### 2. tools_condition
**What it is:** A function that checks if the LLM's response contains tool calls
**Logic:** If yes → route to tools node, If no → route to END

### Implementation

#### Step 1: Create the Graph Structure
```python
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

# Build the graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges("tool_calling_llm", tools_condition)
builder.add_edge("tools", END)

graph = builder.compile()
```

#### Step 2: Define the LLM Node
```python
def tool_calling_llm(state: MessagesState):
    return {"messages": model2_with_tools.invoke(state["messages"])}
```

#### Step 3: Test the Agent
```python
# Test with a question requiring tools
messages = [HumanMessage(content="Hello, what is 2 multiplied by 2?")]
result = graph.invoke({"messages": messages})

for m in result["messages"]:
    m.pretty_print()
```

**Expected Output:**
```
Human Message
Hello, what is 2 multiplied by 2?

AI Message
"I'll help you calculate 2 multiplied by 2."
Tool Calls: multiply(2, 2)

Tool Message
4
```

### Understanding the Flow 🔄

**Graph Flow:**
```
START → tool_calling_llm → tools_condition → tools OR END
```

**Process:**
1. LLM processes user message
2. Checks if tools are needed
3. Executes tools or ends conversation

---

## 8. ReACT Pattern

### What is ReACT? 🔄

**Simple Explanation:** ReACT (Reason + Act) is like having a smart assistant that:
1. **Reasons** about what to do
2. **Acts** by calling a tool
3. **Observes** the result
4. **Repeats** until the task is complete

**Key Difference:** Unlike basic tool calling, ReACT creates a loop where the assistant can see tool results and decide to call more tools.

### ReACT Flow Diagram 📊

```
User Query → Assistant LLM Reasoning
   │
   ▼
Need Tools?
   │
  Yes ──► Execute Tools ──► Observe Result ──► Loop ──► Final Answer
   │
   └──► No ──► Final Answer
```

### Building a ReACT Agent 🛠️

#### Step 1: Define Multiple Tools
```python
def addition(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

def subtraction(a: int, b: int) -> int:
    """Subtracts two numbers"""
    return a - b

def multiplication(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

def division(a: int, b: int) -> int:
    """Divide two numbers"""
    return a / b

# Create model with all tools
model3 = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o",
    max_tokens=512,
    temperature=0.1,
)
tools = [addition, subtraction, multiplication, division]
model3_with_tools = model3.bind_tools(tools)
```

#### Step 2: Create the ReACT Graph
```python
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage

# System message for the assistant
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

def assistant(state: MessagesState):
    return {"messages": model3_with_tools.invoke([sys_msg] + state["messages"])}

# Build the ReACT graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")  # Loop back (key difference!)
react_graph = builder.compile()
```

**Key Point:** Notice `builder.add_edge("tools", "assistant")` - this creates the loop!

#### Step 3: Test Multi-Step Reasoning
```python
# Test with a complex multi-step problem
messages = [HumanMessage(content="Add 3 and 4. Multiply the output by 2. Divide the output by 5")]
result = react_graph.invoke({"messages": messages})

for m in result["messages"]:
    m.pretty_print()
```

**Expected Output:**
```
Human Message
Add 3 and 4. Multiply the output by 2. Divide the output by 5

AI Message
I'll help you perform these arithmetic operations step by step.

Tool Call: addition(3, 4)
Tool Message: 7

AI Message
Now I'll multiply 7 by 2.

Tool Call: multiplication(7, 2)
Tool Message: 14

AI Message
Finally, I'll divide 14 by 5.

Tool Call: division(14, 5)
Tool Message: 2.8

AI Message
The final result is 2.8
To summarize:
3 + 4 = 7
7 × 2 = 14
14 ÷ 5 = 2.8
```

### Understanding ReACT in Action 🎯

**What Happened:**
1. AI reasoned it needed to add 3 and 4
2. Called addition tool, got result 7
3. Reasoned it needed to multiply 7 by 2
4. Called multiplication tool, got result 14
5. Reasoned it needed to divide 14 by 5
6. Called division tool, got result 2.8
7. Provided final answer with summary

**This is ReACT:** Reasoning and acting in a loop!

---

## 9. Memory & Persistence

### Why Memory Matters 🧠

**Problem:** By default, agents start fresh with each query
**Solution:** Memory allows agents to remember previous interactions and maintain context

### How Memory Works in LangGraph 💾

**Simple Explanation:** LangGraph uses "checkpointers" to save state after each step, tied to a conversation session (thread_id).

### Adding Memory to Your Agent

#### Step 1: Set Up Memory
```python
from langgraph.checkpoint.memory import MemorySaver

# Create memory saver
memory = MemorySaver()

# Compile graph with memory
react_graph_memory = builder.compile(checkpointer=memory)
```

#### Step 2: Use Thread IDs
```python
# First conversation
config = {"configurable": {"thread_id": "1"}}
messages = [HumanMessage(content="Add 3 and 4")]
result = react_graph_memory.invoke({"messages": messages}, config)

print("First result:", result["messages"][-1].content)
```

**Expected Output:**
```
First result: The result of 3 + 4 is 7
```

#### Step 3: Continue the Conversation
```python
# Continue the same conversation
messages = [HumanMessage(content="Multiply that by 2.")]
result = react_graph_memory.invoke({"messages": messages}, config)

print("Second result:", result["messages"][-1].content)
```

**Expected Output:**
```
Second result: I'll multiply 7 by 2. The result is 14
```

**Key Point:** The agent remembered "that" referred to the previous result (7)!

### Understanding Memory Benefits 🎯

**What Memory Enables:**
- **Context Awareness:** "Multiply that by 2" works because it remembers the previous result
- **Natural Conversations:** No need to restate everything
- **Stateful Interactions:** Each conversation thread maintains its own state

---

## 10. Real-World Project

### Project: Bank Emissions Assessment Agent 🏦

**Goal:** Build a complete agent that helps a bank track and analyze their operational carbon footprint.

### Business Context 📊

**Scenario:** TechBank International's ESG team needs to track operational emissions across all facilities to achieve net-zero goals.

**Emissions Sources:**
- Real estate (offices, branches)
- Fleet vehicles
- Waste management
- Supply chain vendors

### Step 1: Create Emission Calculation Tools

#### Real Estate Emissions
```python
def calculate_real_estate_emissions(
    square_meters: float,
    energy_intensity: float = 0.05
) -> float:
    """
    Calculate CO2 emissions from real estate operations (offices, branches, data centers).

    Args:
        square_meters: Total square meters of real estate
        energy_intensity: Energy intensity factor (kgCO2 per sqm per year), default 0.05

    Returns:
        Annual CO2 emissions in kg
    """
    emissions = square_meters * energy_intensity * 365
    return round(emissions, 2)
```

#### Fleet Emissions
```python
def calculate_fleet_emissions(km_driven: float, fuel_type: str = "diesel") -> float:
    """
    Calculate CO2 emissions from company fleet vehicles.

    Args:
        km_driven: Total kilometers driven
        fuel_type: Type of fuel used - "diesel", "petrol", or "electric"

    Returns:
        CO2 emissions in kg
    """
    # Emission factors in kg CO2 per km
    emission_factors = {
        "diesel": 0.27,
        "petrol": 0.24,
        "electric": 0.05
    }

    factor = emission_factors.get(fuel_type.lower(), 0.27)
    emissions = km_driven * factor
    return round(emissions, 2)
```

#### Waste Emissions
```python
def calculate_waste_emissions(waste_kg: float, recycling_rate: float = 0.3) -> float:
    """
    Calculate CO2 emissions from waste management.

    Args:
        waste_kg: Total waste in kilograms
        recycling_rate: Percentage of waste recycled (0.0 to 1.0), default 0.3

    Returns:
        CO2 emissions in kg
    """
    # Non-recycled waste has higher emission factor
    non_recycled = waste_kg * (1 - recycling_rate)
    recycled = waste_kg * recycling_rate

    emissions = (non_recycled * 0.5) + (recycled * 0.1)
    return round(emissions, 2)
```

#### Supply Chain Emissions
```python
def calculate_supply_chain_emissions(spend_amount: float, category: str = "services") -> float:
    """
    Calculate estimated CO2 emissions from supply chain spending.

    Args:
        spend_amount: Amount spent with vendors in USD
        category: Category of spending - "services", "goods", or "technology"

    Returns:
        Estimated CO2 emissions in kg
    """
    # Emission factors in kg CO2 per USD spent
    emission_factors = {
        "services": 0.2,
        "goods": 0.5,
        "technology": 0.3
    }

    factor = emission_factors.get(category.lower(), 0.3)
    emissions = spend_amount * factor
    return round(emissions, 2)
```

### Step 2: Test the Tools
```python
# Test all tools
print("🏢 Real Estate Emissions")
print(f"10,000 sqm office: {calculate_real_estate_emissions(10000)} kg CO2/year")

print("\n🚗 Fleet Emissions")
print(f"50,000 km diesel: {calculate_fleet_emissions(50000, 'diesel')} kg CO2")
print(f"50,000 km electric: {calculate_fleet_emissions(50000, 'electric')} kg CO2")

print("\n♻️ Waste Emissions")
print(f"5,000 kg waste (30% recycled): {calculate_waste_emissions(5000, 0.3)} kg CO2")

print("\n📦 Supply Chain Emissions")
print(f"$100,000 spent on services: {calculate_supply_chain_emissions(100000, 'services')} kg CO2")
```

**Expected Output:**
```
🏢 Real Estate Emissions
10,000 sqm office: 182500.0 kg CO2/year

🚗 Fleet Emissions
50,000 km diesel: 13500.0 kg CO2
50,000 km electric: 2500.0 kg CO2

♻️ Waste Emissions
5,000 kg waste (30% recycled): 1900.0 kg CO2

📦 Supply Chain Emissions
$100,000 spent on services: 20000.0 kg CO2
```

### Step 3: Build the Emissions Agent

#### Create Specialized Model
```python
# Create a specialized model for emissions assessment
emissions_model = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="gpt-4o",
    max_tokens=1024,
    temperature=0.1,
)

# Bind all emissions tools
emissions_tools = [
    calculate_real_estate_emissions,
    calculate_fleet_emissions,
    calculate_waste_emissions,
    calculate_supply_chain_emissions
]
emissions_model_with_tools = emissions_model.bind_tools(emissions_tools)

# System message for the emissions agent
emissions_sys_msg = SystemMessage(content="""
You are an ESG (Environmental, Social, Governance) analyst helping a bank achieve net-zero operational emissions.
1. Calculate emissions from various sources (real estate, fleet, waste, supply chain)
2. Break down complex queries into specific calculations
3. Provide the total emissions in kg CO2
4. Offer recommendations for emissions reduction when appropriate
""")
```

#### Define the Assistant Node
```python
def emissions_assistant(state: MessagesState):
    return {"messages": emissions_model_with_tools.invoke([emissions_sys_msg] + state["messages"])}
```

#### Build the Agent Graph
```python
# Build the emissions agent graph
emissions_agent_builder = StateGraph(MessagesState)
emissions_agent_builder.add_node("emissions_assistant", emissions_assistant)
emissions_agent_builder.add_node("tools", ToolNode(emissions_tools))

# Add edges with ReACT loop
emissions_agent_builder.add_edge(START, "emissions_assistant")
emissions_agent_builder.add_conditional_edges("emissions_assistant", tools_condition)
emissions_agent_builder.add_edge("tools", "emissions_assistant")  # ReACT loop

# Compile
emissions_agent = emissions_agent_builder.compile()
```

### Step 4: Test the Agent

#### Test 1: Single Calculation
```python
messages = [HumanMessage(content="Calculate emissions from our London headquarters which is 15,000 square meters")]
result = emissions_agent.invoke({"messages": messages})

for m in result['messages']:
    m.pretty_print()
```

**Expected Output:**
```
Human Message
Calculate emissions from our London headquarters which is 15,000 square meters

AI Message
"I'll calculate the CO2 emissions from your London headquarters using the real estate emissions calculator."

Tool Call:
calculate_real_estate_emissions(square_meters=15000)

Tool Message:
273750.0

AI Message
Real Estate Emissions — London Headquarters:
- Building size: 15,000 sqm
- Annual CO2 emissions: 273,750 kg CO2 (273.75 tonnes CO2)
- Energy intensity factor: 0.05 kgCO2 per sqm per year (default)

Recommendations:
- LED lighting upgrades
- HVAC optimization
- Renewable energy sourcing
- Green certifications (LEED, BREEAM)
```

#### Test 2: Multi-step Calculation
```python
messages = [HumanMessage(content="""
Calculate our total operational emissions from:
- Our fleet that drove 120,000 km on diesel
- Our office waste of 8,000 kg with 40% recycling rate
- Our technology vendor spending of $250,000
""")]
result = emissions_agent.invoke({"messages": messages})

for m in result['messages']:
    m.pretty_print()
```

**Expected Output:**
```
Human Message
Calculate our total operational emissions from:
- Our fleet that drove 120,000 km on diesel
- Our office waste of 8,000 kg with 40% recycling rate
- Our technology vendor spending of $250,000

AI Message
"I'll calculate the total operational emissions by breaking this down into individual calculations for each source."

Tool Call:
calculate_fleet_emissions(120000, diesel)

Tool Message:
32400.0

Tool Call:
calculate_waste_emissions(8000, 0.4)

Tool Message:
2720.0

Tool Call:
calculate_supply_chain_emissions(250000, technology)

Tool Message:
75000.0

AI Message
## Total Operational Emissions Summary

- Fleet (Diesel vehicles): 32,400 kg CO2
- Waste Management: 2,720 kg CO2
- Supply Chain (Technology vendors): 75,000 kg CO2

TOTAL: 110,120 kg CO2 (110.12 tonnes)

Key Observations:
- Supply chain emissions = 68%
- Fleet emissions = 29%
- Waste management = 2.5%

Recommendations:
- Transition fleet to EVs or hybrids
- Evaluate vendor sustainability
- Increase recycling rate above 40%
```

### Step 5: Add Memory for Multi-Turn Conversations

#### Set Up Memory
```python
from langgraph.checkpoint.memory import MemorySaver

# Add memory to the emissions agent
emissions_memory = MemorySaver()
emissions_agent_with_memory = emissions_agent_builder.compile(checkpointer=emissions_memory)
```

#### Test Multi-Turn Conversation
```python
# Turn 1: Initial Assessment
config = {"configurable": {"thread_id": "esg_analyst_001"}}

print("=" * 70)
print("TURN 1: Calculate baseline emissions")
print("=" * 70)

messages = [HumanMessage(content="Calculate emissions from our Manchester branch: 8,500 square meters")]
result = emissions_agent_with_memory.invoke({"messages": messages}, config)

for m in result['messages']:
    m.pretty_print()
```

**Expected Output:**
```
Human Message:
Calculate emissions from our Manchester branch: 8,500 square meters

AI Message:
"I'll calculate the CO2 emissions from your Manchester branch real estate operations."

Tool Call:
calculate_real_estate_emissions(square_meters=8500)

Tool Message:
155125.0

AI Message:
Real Estate Emissions — Manchester Branch:
- Total emissions: 155,125 kg CO2/year
- Source: 8,500 sqm office space
- Energy intensity factor: 0.05 kgCO2/sqm/year

Recommendations:
- LED lighting upgrades
- HVAC automation
- Renewable energy procurement
- Insulation & energy efficiency
- Temperature controls and sensors
```

#### Turn 2: Adding Fleet Emissions (Contextual)
```python
print("=" * 70)
print("TURN 2: Follow-up adding fleet emissions")
print("=" * 70)

messages = [HumanMessage(content="That branch also has a fleet that drove 45,000 km on diesel. Add that to the total.")]
result = emissions_agent_with_memory.invoke({"messages": messages}, config)

# Print only new messages
for m in result['messages'][-3:]:
    m.pretty_print()
```

**Expected Output:**
```
Tool Call:
calculate_fleet_emissions(45000, diesel)

Tool Message: 12150.0

AI Message:
Manchester Branch — Total Emissions Summary:
- Real Estate: 155,125 kg CO2
- Fleet (Diesel): 12,150 kg CO2
TOTAL: 167,275 kg CO2/year (167.3 tonnes)
Breakdown:
- Real Estate: 92.7%
- Fleet: 7.3%

Fleet Recommendations:
- Transition to electric/hybrid
- Carpooling, teleconferencing, maintenance optimization
```

**Key Point:** The agent remembered "that branch" referred to the Manchester branch from Turn 1!

#### Turn 3: Scenario Comparison
```python
print("=" * 70)
print("TURN 3: Scenario comparison using conversation context")
print("=" * 70)

messages = [HumanMessage(content="If we switched that fleet to electric vehicles, how much would our total emissions decrease?")]
result = emissions_agent_with_memory.invoke({"messages": messages}, config)

for m in result['messages'][-4:]:
    m.pretty_print()
```

**Expected Output:**
```
Tool Call:
calculate_fleet_emissions(45000, electric)

Tool Message:
2250.0

AI Message:
Manchester Branch — Electric Fleet Comparison:

Current (Diesel):
- Real estate: 155,125 kg CO2
- Fleet: 12,150 kg CO2
TOTAL: 167,275 kg CO2

With Electric:
- Real estate: 155,125 kg CO2
- Fleet: 2,250 kg CO2
TOTAL: 157,375 kg CO2

Reduction: 9,900 kg CO2 (9.9 tonnes)
Fleet reduction: 81.5%

This switch significantly reduces fleet emissions by over 80%. Even though fleet is a smaller source than buildings, this is still meaningful progress.
```

### Understanding the Power of Memory 🧠

**What Just Happened:**
1. **Turn 1:** Agent calculated Manchester branch real estate emissions
2. **Turn 2:** Agent understood "that branch" and added fleet emissions
3. **Turn 3:** Agent used stored context to compare diesel vs electric scenarios

**This is the power of memory in LangGraph** — enabling dynamic, stateful conversations and tool use!

---

## 11. Advanced Topics

### Real-World Applications 🌍

The same patterns can be applied to:

#### Customer Service Agents 💬
- **Use Case:** Handle customer inquiries, access databases, resolve issues
- **Tools:** CRM lookup, ticket creation, knowledge base search
- **Memory:** Remember customer history and preferences

#### Financial Analysis Agents 📊
- **Use Case:** Generate reports, analyze metrics, provide recommendations
- **Tools:** Data analysis, chart generation, risk calculations
- **Memory:** Track analysis history and trends

#### IT Support Agents 🧰
- **Use Case:** Diagnose issues, query systems, execute fixes
- **Tools:** System monitoring, log analysis, automated repairs
- **Memory:** Track incident history and solutions

#### Legal Research Agents ⚖️
- **Use Case:** Search documents, analyze cases, provide legal insights
- **Tools:** Document search, case law lookup, precedent analysis
- **Memory:** Track research history and findings

#### Healthcare Agents 🏥
- **Use Case:** Review patient data, coordinate treatment, provide insights
- **Tools:** Medical database access, symptom analysis, treatment recommendations
- **Memory:** Track patient history and treatment plans

### Next Steps 🚀

#### 1. Explore Advanced Features
- **Sub-graphs:** Break complex workflows into smaller, manageable pieces
- **Dynamic Nodes:** Create nodes that can be added or removed at runtime
- **Streaming:** Get real-time updates as the agent processes

#### 2. Production Deployment
- **Error Handling:** Add robust error handling and recovery
- **Monitoring:** Implement logging and performance monitoring
- **Scaling:** Deploy with proper infrastructure and load balancing

#### 3. Security & Access Control
- **Authentication:** Implement user authentication and authorization
- **API Security:** Secure your agent endpoints
- **Data Privacy:** Ensure compliance with data protection regulations

#### 4. Advanced Patterns
- **Multi-Agent Systems:** Create agents that work together
- **Hierarchical Agents:** Build agents that manage other agents
- **Adaptive Agents:** Create agents that learn and improve over time

---

## 🎉 Congratulations!

You've completed the LangGraph Complete Training Guide! You now understand:

✅ **State Management** — defining and managing state in graphs
✅ **Nodes & Edges** — building LangGraph workflows  
✅ **Conditional Routing** — making dynamic decisions
✅ **Tool Calling** — giving agents abilities to perform actions
✅ **Reducers** — accumulating state properly
✅ **ReACT Pattern** — building agents that reason and act iteratively
✅ **Memory** — maintaining context across conversations
✅ **Real-World Applications** — building production-ready agents

### Your Learning Journey Continues! 🚀

You now have the foundation to build sophisticated AI agents that can:
- Make intelligent decisions
- Use tools effectively
- Remember context
- Handle complex multi-step problems
- Provide real business value

**Happy coding and agent building!** 🤖✨

---

## 📚 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Python TypedDict Documentation](https://docs.python.org/3/library/typing.html#typing.TypedDict)

---

*This training guide was created to help you master LangGraph and build amazing AI agents. Keep experimenting, keep learning, and keep building!* 🎯
