
📘 LangGraph Basics Tutorial
Welcome!

This tutorial will teach you the fundamental concepts of LangGraph, a framework for building stateful, multi-step applications with Large Language Models (LLMs).

What is LangGraph?

LangGraph allows you to create complex agent workflows by modeling them as graphs.
Each node in the graph represents a step in your workflow, and edges define how data flows between steps.
This makes it perfect for building AI agents that need to:

Make decisions

Use tools

Maintain conversation context

Handle complex multi-step reasoning

What You'll Learn

By the end of this tutorial, you'll understand:

State Management – How to define and manage state in your agent

Nodes & Edges – Building blocks of LangGraph workflows

Conditional Routing – Making dynamic decisions in your agent

Tool Calling – Giving your agent abilities to perform actions

ReACT Pattern – Building agents that reason and act iteratively

Memory – Maintaining context across multiple interactions

🧭 Tutorial Structure

Each concept is introduced with a simple example first, then followed by a real-world banking use case where you'll build a Net Zero Emissions Assessment Agent for a bank tracking their operational carbon footprint.

⚡ Prerequisites

Basic Python knowledge

AWS account with Bedrock access (Claude model)

Familiarity with LLMs and basic AI concepts

🧰 Setup Instructions
Step 1: Create a Virtual Environment

Open your terminal and navigate to this notebook's directory, then create a virtual environment with Python 3.12:

# Create virtual environment
python3.12 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

Step 2: Install Required Packages

Create a requirements.txt file in the same directory with the following contents:

txt
langchain-core
langgraph
langgraph-checkpoint
langgraph-prebuilt
jupyter
ipykernel
langchain-aws
pandas
pydantic
pydantic_core
python-dotenv


Then install the packages:

pip install -r requirements.txt

Step 3: Configure AWS Credentials

Create a .env file in the same directory with your AWS credentials:

BEDROCK_MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here


Note: Make sure your AWS account has access to Amazon Bedrock and the Claude Sonnet 4 model.

Step 4: Launch Jupyter Notebook

Start the Jupyter notebook server:

jupyter notebook


This will open a browser window. Navigate to this notebook and you're ready to go!

🧰 Troubleshooting

Python 3.12 not found? Install it from the official Python site.

AWS Bedrock access issues? Ensure you’ve requested model access in the AWS Bedrock console.

Import errors? Make sure your virtual environment is activated before running Jupyter.

🌱 Basic Set-up — Part 1: Environment Setup

Before we build our agents, we need to set up our environment and connect to the LLM.
We’ll be using AWS Bedrock with Claude Sonnet 4 as our language model.

What’s happening here:

Loading environment variables (API keys, region settings)

Initializing the Claude model via AWS Bedrock

Testing the connection with a simple message

This setup will be used throughout the tutorial.

BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "us.anthropic.claude-sonnet-4-20250514-v1:0")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

model = ChatBedrockConverse(
    model_id=BEDROCK_MODEL_ID,
    region_name=AWS_REGION,
    max_tokens=512,
    temperature=0.1,
)

msg = HumanMessage(content="Hi how are you")
messages = [msg]
model.invoke(messages)

🧠 Part 2: Building Your First Graph

Now let’s understand the core building blocks of LangGraph: State, Nodes, and Edges.

What is a Graph?

A graph in LangGraph is a workflow where:

State: Data that flows through your workflow

Nodes: Functions that process and modify the state

Edges: Connections that determine the flow between nodes

Think of it like a flowchart where each box (node) does something with your data, and arrows (edges) show what happens next.

🧪 Simple Example: Activity Selector

We’ll build a simple graph that decides what activity someone will do based on a random “mood”.

Visual Overview: LangGraph Architecture

State(Data)
    ↓
Node 1 (Function)
    ↓
Conditional Edge (Decision)
   ↙              ↘
Node 2            Node 3

Key Concepts:

State: Your data that flows through the graph

Nodes: Functions that process and transform the state

Edges: Define the execution flow between nodes

Conditional Edges: Make decisions about which node to execute next

🏗️ Step 1: Define State

The State is a TypedDict that defines what data flows through your graph.
Each node can read from and write to the state.

In this example, our state has one field: graph_state which is a string that gets modified by each node.

from typing_extensions import TypedDict

class State(TypedDict):
    graph_state: str

🧱 Step 2: Define Nodes

Nodes are functions that:

Receive the current state

Perform some operation

Return updated state

Each node below adds text to the graph_state string. Node 1 always runs, then either Node 2 or Node 3 runs based on a decision.

def node_1(state):
    print("Node 1")
    return {"graph_state": state["graph_state"] + " will"}

def node_2(state):
    print("Node 2")
    return {"graph_state": state["graph_state"] + " go surfing"}

def node_3(state):
    print("Node 3")
    return {"graph_state": state["graph_state"] + " go rock climbing"}

🧭 Step 3: Define Conditional Edges

Conditional edges allow your graph to make decisions. This function determines which node to execute next based on the current state.

import random
from typing import Literal

def decide_mood_node(state) -> Literal["node_2", "node_3"]:
    user_input = state["graph_state"]
    if random.random() < 0.5:
        return "node_2"
    return "node_3"

🔧 Step 4: Build and Compile the Graph

Now we connect everything together:

Create a StateGraph with our State schema

Add all nodes

Add edges to define the flow

Compile the graph

START → node_1 → (conditional) → node_2 or node_3 → END

from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood_node)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

graph = builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))

🏃 Step 5: Run the Graph

When you invoke the graph:

Initial state is passed in: {"graph_state": "Roshan will"}

Node 1 appends " will"

The conditional edge decides between Node 2 or Node 3

The chosen node appends its text

Final state is returned

graph.invoke({"graph_state": "Roshan will"})

✅ Query Outputs for Emissions Example
Query 1: Fleet vehicle emissions
Classified as: scope_1
Calculating Scope 1 emissions (direct emissions)...
Result: 2300.5 kg CO2

Query 2: Electricity emissions
Classified as: scope_2
Calculating Scope 2 emissions (energy indirect)...
Result: 15000.0 kg CO2

Query 3: Supply chain emissions
Classified as: scope_3
Calculating Scope 3 emissions (supply chain)...
Result: 45000.0 kg CO2

📨 Part 3: Messages and Conversation Flow

In LangGraph, Messages are a special type of state used for conversations with LLMs.
Messages keep track of the conversation history between the user and the AI.

Message Types

HumanMessage: Messages from the user

AIMessage: Responses from the AI model

SystemMessage: Instructions for the AI model

ToolMessage: Results from tool executions

Messages are stored as a list, allowing the LLM to understand context from previous turns in the conversation.

Visual: Message Flow in LangGraph
User ── HumanMessage("Hello") ──> Graph ──> LLM ──> State
                  Add message to state
                           │
                           ▼
                  Invoke with messages
                           │
                           ▼
             AIMessage("Hi there!")
                           │
                           ▼
                   Add AI response
                           │
                           ▼
                  Return updated state


➡ Messages accumulate using add_messages reducer

User <── Graph <── LLM <── State


Messages flow through the graph and accumulate in the state, allowing the LLM to maintain context.

🧾 Code Example
from pprint import pprint
from langchain_core.messages import AIMessage, HumanMessage

messages = [HumanMessage(content="There are 600+ CRR related regulations")]
messages.append(AIMessage(content="Thanks for the information, that is great to know, would you like me to elaborate on any of these"))
messages.append(HumanMessage(content="Give me details of 1 regulation which applies to Barclays"))

for m in messages:
    m.pretty_print()

💬 Example Output
Human Message
There are 600+ CRR related regulations

AI Message
Thanks for the information, that is great to know, would you like me to elaborate on any of these

Human Message
Give me details of 1 regulation which applies to Barclays

🧠 Example: Multi-turn Conversation

Below we'll create a conversation with multiple turns. Notice how each message is added to the list, building up the conversation context.

When you send this list to an LLM, it can understand the full conversation history and provide contextually appropriate responses.

model2 = ChatBedrockConverse(
    model_id=BEDROCK_MODEL_ID,
    region_name=AWS_REGION,
    max_tokens=512,
    temperature=0.1,
)

result = model2.invoke(messages)
print(type(result))
result.pretty_print()

🧾 Example Output
<class 'langchain_core.messages.ai.AIMessage'>
AI Message
Here's a detailed overview of one key CRR regulation that applies to Barclays:

## CRR Article 92 — Own Funds Requirements
**Regulation:** EU Regulation 575/2013, Article 92
**Applies to:** All credit institutions including Barclays plc and Barclays Bank plc

### Key Requirements:
**Minimum Capital Ratios:**
- Common Equity Tier 1 (CET1) ratio: minimum 4.5%
- Tier 1 capital ratio: minimum 6%
- Total capital ratio: minimum 8%

### How it applies to Barclays:
**Current Status (as of recent reports):**
- Barclays maintains CET1 ratios well above minimum requirements
- Typically operates with CET1 ratios around 13–15%
- Must report these ratios quarterly to regulators

**Practical Impact:**
- Determines how much risk-weighted assets Barclays can hold
- Influences lending capacity and business strategy
- Affects dividend distribution capabilities
- Triggers regulatory intervention if breached

**Compliance Mechanisms:**
- Regular stress testing
- Capital planning processes
- Risk appetite frameworks
- Monthly monitoring and reporting

This regulation is fundamental as it directly impacts Barclays' ability to operate, lend, and distribute profits to shareholders.


“Would you like me to elaborate on any specific aspect of this regulation or discuss another CRR article?”

📥 Invoking the Model with Conversation History

When we pass the message list to the model, it processes the entire conversation context and generates an appropriate response based on the history.

result.response_metadata


Sample metadata shows Bedrock model response details and timing.

🛠️ Part 4: Tool Calling

Tools give your LLM agent the ability to take actions! Instead of just generating text, the agent can:

Perform calculations

Query databases

Call APIs

Execute functions

How Tool Calling Works

You define Python functions and bind them to your model.

The model decides when to use a tool based on the user’s query.

The model generates a tool call with the appropriate parameters.

Your code executes the function and returns the result.

The model uses the result to formulate its final response.

Visual: Tool Calling Flow
User          LLM              ToolNode          Function
"Calculate 4 × 6"
        Analyze query
        ───────────────────────────────► tool_call(multiply, a=4, b=6)
                                        stopReason: 'tool_use'
                                        ───────► Execute multiply(4, 6)
                                                        Return 24
◄──────────────────────────────────── ToolMessage(result=24)
"The result is 24"
stopReason: 'end_turn'

🧮 Tool Calling Process

User asks a question requiring computation.

LLM recognizes it needs a tool.

LLM generates structured tool call.

ToolNode executes the function.

Result is returned to LLM.

LLM formulates final response.

def multiply(a: int, b: int) -> int:
    """
    Multiple two numbers and returns a integer
    Args:
        a: first integer
        b: second integer
    """
    return a * b

model2_with_tools = model2.bind_tools([multiply])
model2_with_tools([HumanMessage(content="Hello")])

🧰 Define a Tool

A tool is just a Python function with:

Type hints for parameters

A docstring explaining what it does and describing the parameters

The docstring is important! The LLM reads it to understand when and how to use the tool.

result2 = model2_with_tools.invoke([HumanMessage(content="What is 4 times 6?")])


Sample AI Response:

"I'll calculate 4 times 6 for you..."
Tool call: multiply(a=4, b=6)
ToolMessage(result=24)

🧪 Testing Tool Calls

When you ask a question that requires the tool, the model:

Recognizes it needs to use a tool

Generates a tool_call with the function name and arguments

Waits for you to execute the function and return the result

stopReason: 'tool_use' means the model is requesting a tool execution, not ending the conversation.

result2.response_metadata
result2.tool_calls

📊 Inspecting Tool Calls

The tool_calls attribute contains all the information needed to execute the function:

name: Which function to call

args: The arguments to pass

id: Unique identifier for this tool call

This structured format allows LangGraph to automatically handle tool execution.

🧭 Part 5: State Management with Reducers

When working with messages in LangGraph, we need a way to accumulate messages instead of replacing them. This is where reducers come in.

The Problem

By default, when a node returns state, it replaces the old value:

class MessagesState(TypedDict):
    messages: List[AnyMessage]  # This would REPLACE messages


If node 1 adds a message and node 2 adds another, we’d lose node 1’s message!

The Solution: Reducers

A reducer is a function that defines how to merge new state with existing state.

from typing import TypedDict
from langchain_core.messages import AnyMessage

class MessagesState(TypedDict):
    messages: list[AnyMessage]


We ideally want to append new messages, not replace them.

🧩 Using the add_messages Reducer

The add_messages reducer appends new messages to the existing list instead of replacing it.
This is done using Python’s Annotated type hint:

messages: Annotated[list[AnyMessage], add_messages]


This tells LangGraph:

“When updating messages, use the add_messages function to merge old and new values.”

from typing import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

🧠 How add_messages Works

It takes the current state and new messages, then combines them into a single list.

initial_messages = [HumanMessage(content="Hi how are you"),
                    AIMessage(content="I am good, thank you")]

new_message = [HumanMessage(content="What is the role of PRA in banking")]

add_messages(initial_messages, new_message)


Output:

[HumanMessage("Hi how are you"),
 AIMessage("I am good, thank you"),
 HumanMessage("What is the role of PRA in banking")]

🌍 Real-World Example: Bank Emissions Calculator Tools

Now let’s create tools that a bank would actually use to calculate their operational emissions.
These tools will calculate emissions from different sources.

Scenario: The bank needs to track emissions from:

Real estate (offices, branches)

Fleet vehicles

Waste management

Supply chain vendors

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

    🏢 Emissions Calculator — Additional Functions
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


✅ print("✅ Emissions calculator tools defined!")

🧪 Test the Emissions Tools

Let's test our tools directly before integrating them with an agent.

# Test 1: Real estate emissions
print("🏢 Real Estate Emissions")
print(f"10,000 sqm office: {calculate_real_estate_emissions(10000)} kg CO2/year\n")

# Test 2: Fleet emissions
print("🚗 Fleet Emissions")
print(f"50,000 km diesel: {calculate_fleet_emissions(50000, 'diesel')} kg CO2")
print(f"50,000 km electric: {calculate_fleet_emissions(50000, 'electric')} kg CO2\n")

# Test 3: Waste emissions
print("♻️ Waste Emissions")
print(f"5,000 kg waste (30% recycled): {calculate_waste_emissions(5000, 0.3)} kg CO2")
print(f"5,000 kg waste (70% recycled): {calculate_waste_emissions(5000, 0.7)} kg CO2\n")

# Test 4: Supply chain emissions
print("📦 Supply Chain Emissions")
print(f"$100,000 spent on services: {calculate_supply_chain_emissions(100000, 'services')} kg CO2")
print(f"$100,000 spent on goods: {calculate_supply_chain_emissions(100000, 'goods')} kg CO2")

Output:
Real Estate Emissions
10,000 sqm office: 182500.0 kg CO2/year

Fleet Emissions
50,000 km diesel: 13500.0 kg CO2
50,000 km electric: 2500.0 kg CO2

Waste Emissions
5,000 kg waste (30% recycled): 1900.0 kg CO2
5,000 kg waste (70% recycled): 1100.0 kg CO2

Supply Chain Emissions
$100,000 spent on services: 20000.0 kg CO2
$100,000 spent on goods: 50000.0 kg CO2

🧠 Integrating Tools in LangGraph
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

class MessagesState(MessagesState):
    pass

🪄 Building a Basic Tool Calling Graph
_start_
   ↓
tool_calling_llm
   ↓
_end_

builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_edge(START, "tool_calling_llm")
builder.add_edge("tool_calling_llm", END)
graph = builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))

✨ Running the Tool Calling Graph
messages = graph.invoke({"messages": HumanMessage(content="Hello")})
messages


Sample output:

HumanMessage("Hello")
AIMessage("Hello! I'm here to help you...")

messages = graph.invoke({"messages": HumanMessage(content="What is 620 times 2")})
messages

AIMessage("I'll calculate 620 times 2 for you.")
ToolCall: multiply(620, 2)
ToolMessage(1240)

🧰 Part 6: Building Complete Agents with ToolNode

So far we've seen individual components. Now let’s put everything together to build a complete agent that can:

Receive questions

Decide which tools to use

Execute tools

Return results

Introducing ToolNode

ToolNode is a pre-built LangGraph component that:

Automatically executes tool calls from the LLM

Handles errors

Returns results as ToolMessages

This saves you from manually implementing tool execution logic.

Conditional Routing with tools_condition

The tools_condition function automatically checks if the LLM's response contains tool calls:

If yes → routes to the tools node for execution

If no → routes to END (the LLM is done responding)

This creates a simple but powerful pattern for tool-using agents.

from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

🔧 Build the Graph with ToolNode
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges("tool_calling_llm", tools_condition)
builder.add_edge("tools", END)

graph = builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))

🧭 Graph Flow
START → tool_calling_llm → tools_condition → tools OR END


LLM processes user message

Checks if tools are needed

Executes or ends

📊 Sample Run
messages = [HumanMessage(content="Hello, what is 2 multiplied by 2?")]
messages = graph.invoke({"messages": messages})

for m in messages["messages"]:
    m.pretty_print()

Output:
Human Message
Hello, what is 2 multiplied by 2?

AI Message
"I'll help you calculate 2 multiplied by 2."
Tool Calls: multiply(2, 2)
Tool Message: 4

🤖 Part 7: The ReACT Pattern

ReACT (Reason + Act) is a powerful agent pattern where the LLM:

Reasons about what to do

Acts by calling a tool

Observes the result

Repeats until the task is complete

This allows agents to solve complex, multi-step problems.

Key Difference

In the previous example, the graph ended after tool execution.
In ReACT, we create a loop:

tools → assistant (not END!)


This allows the assistant to:

See the tool results

Reason about them

Call more tools if needed

Provide a final answer when done

Visual: ReACT Flow
User Query → Assistant LLM Reasoning
   │
   ▼
Need Tools?
   │
  Yes ──► Execute Tools ──► Observe Result ──► Loop ──► Final Answer
   │
   └──► No ──► Final Answer

ReACT Flow Steps:

Reason: LLM analyzes the query

Act: Decides to use a tool

Observe: Sees the tool result

Loop: Repeats until task is complete

Respond: Provides final answer

🧮 Simple Example: Multi-Step Arithmetic

This ReACT agent can handle queries like:

“Add 3 and 4, multiply the result by 2, then divide by 5.”

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

model3 = ChatBedrockConverse(
    model_id=BEDROCK_MODEL_ID,
    region_name=AWS_REGION,
    max_tokens=512,
    temperature=0.1,
)

tools = [addition, subtraction, multiplication, division]
model3_with_tools = model3.bind_tools(tools)

🧠 Creating the ReACT Graph
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage

sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

def assistant(state: MessagesState):
    return {"messages": model3_with_tools.invoke([sys_msg] + state["messages"])}

from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from IPython.display import Image, display

builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")  # Loop back
react_graph = builder.compile()
display(Image(react_graph.get_graph(xray=True).draw_mermaid_png()))

🔁 ReACT Loop Explanation
START → assistant → tools_condition → tools → assistant → END


Assistant processes the user query

Tools_condition decides if a tool is required

Tools execute

Assistant loops back to reason again if needed

🧮 Run Example
messages = [HumanMessage(content="Add 3 and 4. Multiply the output by 2. Divide the output by 5")]
messages = react_graph.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()

Output Breakdown:
Human Message
Add 3 and 4. Multiply the output by 2. Divide the output by 5

AI Message
I'll help you perform these arithmetic operations step by step.

Tool Call 1: addition(3, 4) → Tool Message: 7
Tool Call 2: multiplication(7, 2) → Tool Message: 14
Tool Call 3: division(14, 5) → Tool Message: 2.8

AI Message
The final result is 2.8
To summarize:
3 + 4 = 7
7 × 2 = 14
14 ÷ 5 = 2.8

🌀 Watching the ReACT Pattern in Action

Observe how the agent:

Calls addition tool

Sees the result (7)

Calls multiplication tool with that result

Sees the result (14)

Calls division tool

Provides the final answer (2.8)

🧠 This is ReACT: reasoning and acting in a loop!

🏦 Complete Example: Bank Net Zero Emissions Agent

We now build a complete emissions assessment agent for a bank.
This agent can:

Calculate emissions from multiple sources

Handle complex queries like “Calculate total emissions from our London office and fleet”

Provide recommendations for reducing emissions.

Scenario:
The bank’s ESG (Environmental, Social, Governance) team needs to track operational emissions across all their facilities and operations to achieve net-zero goals.

# Create a specialized model for emissions assessment
emissions_model = ChatBedrockConverse(
    model_id=BEDROCK_MODEL_ID,
    region_name=AWS_REGION,
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

🧠 Define the Assistant Node
def emissions_assistant(state: MessagesState):
    return {"messages": emissions_model_with_tools.invoke([emissions_sys_msg] + state["messages"])}


✅ print("✅ Emissions assessment agent configured!")

🕸️ Build the Emissions Agent Graph
emissions_agent_builder = StateGraph(MessagesState)
emissions_agent_builder.add_node("emissions_assistant", emissions_assistant)
emissions_agent_builder.add_node("tools", ToolNode(emissions_tools))

# Add edges with ReACT loop
emissions_agent_builder.add_edge(START, "emissions_assistant")
emissions_agent_builder.add_conditional_edges("emissions_assistant", tools_condition)
emissions_agent_builder.add_edge("tools", "emissions_assistant")  # ReACT loop

# Compile
emissions_agent = emissions_agent_builder.compile()

# Visualize
display(Image(emissions_agent.get_graph(xray=True).draw_mermaid_png()))

_start_
   ↓
emissions_assistant
  ↘         ↙
 tools     _end_

🧪 Test the Emissions Agent
Test 1: Single Calculation
messages = [HumanMessage(content="Calculate emissions from our London headquarters which is 15,000 square meters")]
result = emissions_agent.invoke({"messages": messages})

🧾 Sample Output
QUERY 1: Single source emissions

Human Message
Calculate emissions from our London headquarters which is 15,000 square meters

AI Message
"I'll calculate the CO2 emissions from your London headquarters using the real estate emissions calculator."
Tool Call:
calculate_real_estate_emissions(square_meters=15000)
Tool Message: 273750.0

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

🧮 Test 2: Multi-step Calculation
messages = [HumanMessage(content="""
Calculate our total operational emissions from:
- Our fleet that drove 120,000 km on diesel
- Our office waste of 8,000 kg with 40% recycling rate
- Our technology vendor spending of $250,000
""")]
result = emissions_agent.invoke({"messages": messages})

Tool Calls:
calculate_fleet_emissions(120000, diesel)
calculate_waste_emissions(8000, 0.4)
calculate_supply_chain_emissions(250000, technology)

Tool Results:
Fleet emissions: 32400.0 kg CO2
Waste emissions: 2720.0 kg CO2
Supply chain emissions: 75000.0 kg CO2

AI Message:
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

🆚 Test 3: Comparison Query
messages = [HumanMessage(content="""
We're deciding on fleet upgrades. Compare emissions for 75,000 km driven with:
1. Diesel vehicles
2. Electric vehicles

Which would reduce our emissions more?
""")]
result = emissions_agent.invoke({"messages": messages})

Tool Calls:
calculate_fleet_emissions(75000, diesel)
calculate_fleet_emissions(75000, electric)

Results:
Diesel: 20250.0 kg CO2
Electric: 3750.0 kg CO2

AI Message:
Fleet Emissions Comparison for 75,000 km:

- Diesel: 20,250 kg CO2
- Electric: 3,750 kg CO2
- Emission reduction: 16,500 kg CO2 (81.5%)

Recommendations:
- Transitioning to electric fleet would cut emissions substantially.
- Lower operational costs and better alignment with net-zero commitments.

🧠 Part 8: Adding Memory to Agents

By default, the agent starts fresh with each query.
With memory (persistence / checkpointing), agents can:

Remember previous interactions

Maintain context across multiple queries

Continue conversations naturally

How Memory Works in LangGraph

LangGraph uses checkpointers to save state after each step.
This state is tied to a thread_id, representing a conversation session.

from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
react_graph_memory = builder.compile(checkpointer=memory)

🧠 Setting Up Memory
config = {"configurable": {"thread_id": "1"}}
messages = [HumanMessage(content="Add 3 and 4")]
messages = react_graph_memory.invoke({"messages": messages}, config)


Result:

Tool Call: addition(3, 4)
Tool Message: 7

🧠 Using Thread IDs
messages = [HumanMessage(content="Multiply that by 2.")]
messages = react_graph_memory.invoke({"messages": messages}, config)


Result:

Tool Call: multiplication(7, 2)
Tool Message: 14


✅ The agent remembered the previous result without us restating it.

Message history now includes:

Original question (“Add 3 and 4”)

Tool calls & results

New question (“Multiply that by 2”)

Agent’s reasoning using previous state

🧠 This is the power of memory in LangGraph — enabling dynamic, stateful conversations and tool use.

🧭 Real-World Example: Emissions Agent with Memory

We now extend our emissions agent with memory, so ESG analysts can have natural multi-turn conversations about emissions tracking.

# Add memory to the emissions agent
from langgraph.checkpoint.memory import MemorySaver

emissions_memory = MemorySaver()
emissions_agent_with_memory = emissions_agent_builder.compile(checkpointer=emissions_memory)

print("✅ Emissions agent with memory ready!")


✅ Emissions agent with memory ready!

🧪 Scenario: Multi-Turn ESG Analysis Conversation

An ESG analyst wants to assess emissions and explore reduction scenarios across multiple queries.

Turn 1 — Initial Assessment
config = {"configurable": {"thread_id": "esg_analyst_001"}}

print("=" * 70)
print("TURN 1: Calculate baseline emissions")
print("=" * 70)

messages = [HumanMessage(content="Calculate emissions from our Manchester branch: 8,500 square meters")]
result = emissions_agent_with_memory.invoke({"messages": messages}, config)
for m in result['messages']:
    m.pretty_print()

Output:
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

🔁 Turn 2 — Adding Fleet Emissions (Contextual)

Notice how we can refer back to “that branch” without restating details.

print("=" * 70)
print("TURN 2: Follow-up adding fleet emissions")
print("=" * 70)

messages = [HumanMessage(content="That branch also has a fleet that drove 45,000 km on diesel. Add that to the total.")]
result = emissions_agent_with_memory.invoke({"messages": messages}, config)

# print only new messages
for m in result['messages'][-3:]:
    m.pretty_print()

Output:
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

🆚 Turn 3 — Scenario Comparison Using Memory Context
print("=" * 70)
print("TURN 3: Scenario comparison using conversation context")
print("=" * 70)

messages = [HumanMessage(content="If we switched that fleet to electric vehicles, how much would our total emissions decrease?")]
result = emissions_agent_with_memory.invoke({"messages": messages}, config)

for m in result['messages'][-4:]:
    m.pretty_print()

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

🧠 What Just Happened?

Notice how the agent:

Remembered the Manchester branch from Turn 1

Understood “that branch” in Turn 2

Calculated the combined total from previous steps

Compared scenarios in Turn 3 using stored context

🥳 Congratulations!

You've completed the LangGraph basics tutorial.
You now understand:

✅ State Management — defining and managing state in graphs
✅ Nodes & Edges — building LangGraph workflows
✅ Conditional Routing — making dynamic decisions
✅ Tool Calling — giving agents abilities to perform actions
✅ Reducers — accumulating state (e.g., messages) properly
✅ ReACT Pattern — building agents that reason and act iteratively
✅ Memory — maintaining context across conversations

🌍 Real-World Applications

The same pattern can be applied to:

💬 Customer Service Agents — inquiries, database access, issue resolution

📊 Financial Analysis Agents — metrics, reports, recommendations

🧰 IT Support Agents — diagnose, query systems, execute fixes

⚖️ Legal Research Agents — document search, case analysis

🏥 Healthcare Agents — patient data review, treatment coordination

🚀 Next Steps

Explore advanced LangGraph features (sub-graphs, dynamic nodes, streaming)

Build your own agent for your use case

Deploy agents to production with checkpointing

Add error handling and monitoring

Implement authentication & access control

Take part in the CIO Sustainability Hackathon 🏆

