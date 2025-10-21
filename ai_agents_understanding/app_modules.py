import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import json
from datetime import datetime

def show_ai_agent_fundamentals():
    """Display AI agent fundamentals with step-by-step learning"""
    
    st.markdown('<h2 class="section-header">🏗️ AI Agent Fundamentals</h2>', unsafe_allow_html=True)
    
    # Step 1: What are AI Agents?
    st.markdown('<h3 class="step-header">Step 1: Understanding AI Agents</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **An AI Agent is an autonomous software entity that can:**
        
        - **Perceive** its environment through sensors/data inputs
        - **Reason** about the information it receives  
        - **Act** upon the environment through tools/functions
        - **Learn** from its experiences and improve over time
        
        **Key Characteristics:**
        - **Autonomous**: Operates independently
        - **Reactive**: Responds to environmental changes
        - **Proactive**: Takes initiative when appropriate
        - **Social**: Can interact with other agents
        """)
    
    with col2:
        # Agent loop visualization
        fig = go.Figure()
        
        # Add nodes
        nodes = [
            {"x": 0, "y": 0, "label": "Perceive", "color": "#3498db"},
            {"x": 2, "y": 0, "label": "Reason", "color": "#e74c3c"},
            {"x": 4, "y": 0, "label": "Act", "color": "#2ecc71"},
            {"x": 2, "y": -1, "label": "Learn", "color": "#f39c12"}
        ]
        
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[node["x"]], 
                y=[node["y"]], 
                mode='markers+text',
                marker=dict(size=60, color=node["color"]),
                text=node["label"],
                textposition="middle center",
                textfont=dict(color="white", size=12),
                showlegend=False
            ))
        
        # Add arrows
        arrows = [
            {"x0": 0.3, "y0": 0, "x1": 1.7, "y1": 0},
            {"x0": 2.3, "y0": 0, "x1": 3.7, "y1": 0},
            {"x0": 4, "y0": -0.3, "x1": 2, "y1": -0.7},
            {"x0": 2, "y0": -0.3, "x1": 0, "y1": 0}
        ]
        
        for arrow in arrows:
            fig.add_annotation(
                x=arrow["x1"], y=arrow["y1"],
                ax=arrow["x0"], ay=arrow["y0"],
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=3,
                arrowcolor="#666"
            )
        
        fig.update_layout(
            title="The Agent Loop",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Step 2: Agent Types
    st.markdown('<h3 class="step-header">Step 2: Types of AI Agents</h3>', unsafe_allow_html=True)
    
    agent_types = {
        "Type": ["Reactive", "Deliberative", "Hybrid", "Learning", "Multi-Agent"],
        "Description": [
            "Respond to current state only, no memory",
            "Plan before acting, use internal models", 
            "Combine reactive and deliberative approaches",
            "Learn and adapt from experience",
            "Multiple agents working together"
        ],
        "Use Case": [
            "Simple automation, real-time systems",
            "Complex planning, strategic decisions",
            "Most practical applications",
            "Personalization, optimization",
            "Distributed systems, collaboration"
        ],
        "Example": [
            "Thermostat, simple chatbots",
            "Chess AI, route planning",
            "Personal assistants, game AI",
            "Recommendation systems, trading bots",
            "Swarm robotics, distributed computing"
        ]
    }
    
    df_agents = pd.DataFrame(agent_types)
    st.dataframe(df_agents, use_container_width=True)
    
    # Step 3: Agent Components
    st.markdown('<h3 class="step-header">Step 3: Core Components</h3>', unsafe_allow_html=True)
    
    components = {
        "Component": [
            "Perception System",
            "Reasoning Engine", 
            "Action System",
            "Memory System",
            "Learning Module",
            "Communication Interface"
        ],
        "Purpose": [
            "Process and interpret input data",
            "Analyze information and make decisions",
            "Execute actions and interact with environment",
            "Store and retrieve information",
            "Improve performance over time",
            "Communicate with other agents/users"
        ],
        "Implementation": [
            "Sensors, data processors, filters",
            "LLMs, rule engines, neural networks",
            "Tools, APIs, actuators",
            "Databases, vector stores, caches",
            "Reinforcement learning, supervised learning",
            "Message passing, APIs, protocols"
        ]
    }
    
    df_components = pd.DataFrame(components)
    st.dataframe(df_components, use_container_width=True)

def show_agent_architectures():
    """Display different agent architectures and patterns"""
    
    st.markdown('<h2 class="section-header">🏛️ Agent Architectures & Patterns</h2>', unsafe_allow_html=True)
    
    # Single Agent Architecture
    st.markdown('<h3 class="step-header">Single Agent Architecture</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Basic Structure:**
        - One agent handles all tasks
        - Simple to implement and debug
        - Good for focused applications
        - Limited scalability
        
        **Components:**
        - Perception layer
        - Reasoning engine
        - Action execution
        - Memory system
        """)
    
    with col2:
        # Single agent diagram
        fig = go.Figure()
        
        # Add components
        components = [
            {"x": 0, "y": 2, "label": "Environment", "color": "#ecf0f1"},
            {"x": 0, "y": 1, "label": "Perception", "color": "#3498db"},
            {"x": 0, "y": 0, "label": "Reasoning", "color": "#e74c3c"},
            {"x": 0, "y": -1, "label": "Action", "color": "#2ecc71"},
            {"x": 0, "y": -2, "label": "Memory", "color": "#f39c12"}
        ]
        
        for comp in components:
            fig.add_trace(go.Scatter(
                x=[comp["x"]], 
                y=[comp["y"]], 
                mode='markers+text',
                marker=dict(size=50, color=comp["color"]),
                text=comp["label"],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
        
        # Add connections
        for i in range(len(components)-1):
            fig.add_annotation(
                x=0, y=components[i+1]["y"]+0.3,
                ax=0, ay=components[i]["y"]-0.3,
                showarrow=True,
                arrowhead=2,
                arrowcolor="#666"
            )
        
        fig.update_layout(
            title="Single Agent Architecture",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=400,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Multi-Agent Systems
    st.markdown('<h3 class="step-header">Multi-Agent Systems</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Collaboration Patterns:**
        
        **Master-Worker:**
        - One master coordinates workers
        - Good for parallel processing
        - Centralized control
        
        **Peer-to-Peer:**
        - Equal agents collaborate
        - Decentralized decision making
        - More resilient
        
        **Hierarchical:**
        - Multiple levels of agents
        - Complex coordination
        - Scalable structure
        """)
    
    with col2:
        # Multi-agent diagram
        fig = go.Figure()
        
        # Master
        fig.add_trace(go.Scatter(
            x=[0], y=[2], mode='markers+text',
            marker=dict(size=60, color="#e74c3c"),
            text=["Master Agent"],
            textposition="middle center",
            textfont=dict(color="white", size=12),
            showlegend=False
        ))
        
        # Workers
        for i in range(3):
            fig.add_trace(go.Scatter(
                x=[i-1], y=[0], mode='markers+text',
                marker=dict(size=40, color="#3498db"),
                text=[f"Worker {i+1}"],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
            
            # Connection to master
            fig.add_annotation(
                x=0, y=1.7, ax=i-1, ay=0.3,
                showarrow=True, arrowhead=2, arrowcolor="#666"
            )
        
        fig.update_layout(
            title="Multi-Agent System (Master-Worker)",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Architecture Comparison
    st.markdown('<h3 class="step-header">Architecture Comparison</h3>', unsafe_allow_html=True)
    
    comparison_data = {
        "Architecture": ["Single Agent", "Master-Worker", "Peer-to-Peer", "Hierarchical"],
        "Complexity": ["Low", "Medium", "High", "Very High"],
        "Scalability": ["Low", "High", "Medium", "Very High"],
        "Fault Tolerance": ["Low", "Medium", "High", "High"],
        "Coordination": ["None", "Centralized", "Distributed", "Mixed"],
        "Use Cases": [
            "Simple tasks, prototypes",
            "Parallel processing, batch jobs",
            "Distributed systems, consensus",
            "Large organizations, complex domains"
        ]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)

def show_implementation_patterns():
    """Display implementation patterns and code examples"""
    
    st.markdown('<h2 class="section-header">⚙️ Implementation Patterns</h2>', unsafe_allow_html=True)
    
    # ReACT Pattern
    st.markdown('<h3 class="step-header">ReACT Pattern Implementation</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **ReACT (Reason + Act) Pattern:**
    
    The ReACT pattern is one of the most powerful agent patterns where the agent:
    1. **Reasons** about what to do
    2. **Acts** by calling a tool
    3. **Observes** the result
    4. **Repeats** until the task is complete
    """)
    
    # Code example
    st.markdown("**Implementation Example:**")
    st.code("""
class ReACTAgent:
    def __init__(self, llm, tools, memory):
        self.llm = llm
        self.tools = {tool.name: tool for tool in tools}
        self.memory = memory
        self.max_iterations = 10
    
    def run(self, query):
        thoughts = []
        actions = []
        observations = []
        
        for i in range(self.max_iterations):
            # Reason: Generate thought
            thought = self.reason(query, thoughts, actions, observations)
            thoughts.append(thought)
            
            # Check if we should act
            if self.should_act(thought):
                # Act: Choose and execute tool
                action = self.act(thought, query)
                actions.append(action)
                
                # Observe: Get result
                observation = self.observe(action)
                observations.append(observation)
                
                # Check if we're done
                if self.is_final_answer(observation):
                    break
            else:
                # We have a final answer
                break
        
        return self.generate_final_answer(thoughts, actions, observations)
    """, language="python")
    
    # Tool System
    st.markdown('<h3 class="step-header">Tool System Implementation</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Tools give agents the ability to take actions:**
    - Perform calculations
    - Query databases
    - Call APIs
    - Execute functions
    """)
    
    st.code("""
class Tool(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def execute(self, parameters: Dict[str, Any]) -> Any:
        pass
    
    @abstractmethod
    def get_schema(self) -> Dict[str, Any]:
        pass

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("calculator", "Performs mathematical calculations")
    
    def execute(self, parameters: Dict[str, Any]) -> Any:
        operation = parameters.get('operation')
        a = parameters.get('a')
        b = parameters.get('b')
        
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            return a / b if b != 0 else "Error: Division by zero"
        else:
            return "Error: Unknown operation"
    """, language="python")
    
    # Memory System
    st.markdown('<h3 class="step-header">Memory System Implementation</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Short-term Memory:**
        - Recent interactions
        - Current context
        - Temporary storage
        - Fast access
        """)
    
    with col2:
        st.markdown("""
        **Long-term Memory:**
        - Historical data
        - Learned patterns
        - Persistent storage
        - Semantic search
        """)
    
    st.code("""
class ShortTermMemory:
    def __init__(self, max_size: int = 100):
        self.memory = []
        self.max_size = max_size
    
    def add(self, item: Any):
        self.memory.append(item)
        if len(self.memory) > self.max_size:
            self.memory.pop(0)  # Remove oldest item
    
    def get_recent(self, n: int = 10) -> List[Any]:
        return self.memory[-n:]

class LongTermMemory:
    def __init__(self, vector_store):
        self.vector_store = vector_store
    
    def store(self, content: str, metadata: Dict[str, Any] = None):
        embedding = self.vector_store.embed(content)
        self.vector_store.add(embedding, content, metadata or {})
    
    def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        query_embedding = self.vector_store.embed(query)
        results = self.vector_store.search(query_embedding, top_k)
        return results
    """, language="python")

def show_advanced_techniques():
    """Display advanced agent techniques"""
    
    st.markdown('<h2 class="section-header">🚀 Advanced Techniques</h2>', unsafe_allow_html=True)
    
    # Planning and Goal Decomposition
    st.markdown('<h3 class="step-header">Planning and Goal Decomposition</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Hierarchical Planning:**
    - Break down complex goals into sub-goals
    - Create abstract plans at high levels
    - Refine plans at lower levels
    - Handle dependencies between tasks
    """)
    
    st.code("""
class HierarchicalPlanner:
    def __init__(self, llm):
        self.llm = llm
        self.plan_hierarchy = {}
    
    def create_plan(self, goal: str, context: Dict[str, Any]) -> Dict[str, Any]:
        # High-level plan
        high_level_plan = self.create_high_level_plan(goal, context)
        
        # Decompose into sub-plans
        sub_plans = []
        for step in high_level_plan["steps"]:
            if step["complexity"] > 0.7:  # Complex step needs decomposition
                sub_plan = self.decompose_step(step, context)
                sub_plans.append(sub_plan)
            else:
                sub_plans.append(step)
        
        return {
            "goal": goal,
            "high_level_plan": high_level_plan,
            "detailed_plan": sub_plans,
            "estimated_duration": self.estimate_duration(sub_plans)
        }
    """, language="python")
    
    # Multi-Modal Agents
    st.markdown('<h3 class="step-header">Multi-Modal Agents</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Multi-Modal Perception:**
    - Process text, images, audio, video
    - Combine different modalities
    - Generate unified understanding
    - Take appropriate actions
    """)
    
    st.code("""
class MultiModalAgent:
    def __init__(self, llm, tools, perception):
        self.llm = llm
        self.tools = tools
        self.perception = perception
    
    def process_multimodal_input(self, inputs: Dict[str, Any]):
        # Process all modalities
        processed = self.perception.process(inputs)
        
        # Combine modalities for reasoning
        combined_context = self.combine_modalities(processed)
        
        # Generate response
        response = self.llm.generate(combined_context)
        
        return response
    """, language="python")
    
    # Adaptive Learning
    st.markdown('<h3 class="step-header">Adaptive Learning</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Online Learning:**
    - Learn from each interaction
    - Adapt behavior based on performance
    - Update strategy weights
    - Improve over time
    """)
    
    st.code("""
class AdaptiveLearningAgent:
    def __init__(self, base_agent, learning_rate=0.1):
        self.base_agent = base_agent
        self.learning_rate = learning_rate
        self.performance_history = []
        self.strategy_weights = {}
    
    def learn_from_experience(self, experience: Dict[str, Any]):
        # Extract performance metrics
        performance = self.evaluate_performance(experience)
        self.performance_history.append(performance)
        
        # Update strategy weights
        self.update_strategy_weights(performance)
        
        # Adapt agent behavior
        self.adapt_agent_behavior()
    """, language="python")

def show_production_considerations():
    """Display production considerations and best practices"""
    
    st.markdown('<h2 class="section-header">🏭 Production Considerations</h2>', unsafe_allow_html=True)
    
    # Scalability
    st.markdown('<h3 class="step-header">Scalability and Performance</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Agent Pool Management:**
        - Manage multiple agent instances
        - Load balancing across agents
        - Auto-scaling based on demand
        - Resource optimization
        """)
    
    with col2:
        st.markdown("""
        **Performance Optimization:**
        - Caching strategies
        - Connection pooling
        - Asynchronous processing
        - Memory management
        """)
    
    # Monitoring and Observability
    st.markdown('<h3 class="step-header">Monitoring and Observability</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Key Metrics to Monitor:**
    - Request throughput and latency
    - Error rates and types
    - Tool usage patterns
    - Memory and CPU usage
    - User satisfaction scores
    """)
    
    # Health Checks
    st.markdown('<h3 class="step-header">Health Checks and Alerts</h3>', unsafe_allow_html=True)
    
    health_checks = {
        "Check Type": [
            "Response Time",
            "Error Rate",
            "Memory Usage",
            "CPU Usage",
            "Tool Availability",
            "Database Connectivity"
        ],
        "Threshold": [
            "< 5 seconds",
            "< 5%",
            "< 80%",
            "< 70%",
            "All tools responding",
            "Connection successful"
        ],
        "Action": [
            "Scale up if exceeded",
            "Alert and investigate",
            "Restart if critical",
            "Scale horizontally",
            "Restart failed tools",
            "Failover to backup"
        ]
    }
    
    df_health = pd.DataFrame(health_checks)
    st.dataframe(df_health, use_container_width=True)
    
    # Security Considerations
    st.markdown('<h3 class="step-header">Security Considerations</h3>', unsafe_allow_html=True)
    
    security_aspects = {
        "Aspect": [
            "Input Validation",
            "Output Sanitization",
            "Tool Access Control",
            "Data Encryption",
            "Audit Logging",
            "Rate Limiting"
        ],
        "Implementation": [
            "Validate all inputs",
            "Sanitize outputs",
            "Role-based access",
            "Encrypt sensitive data",
            "Log all actions",
            "Limit requests per user"
        ],
        "Tools": [
            "Pydantic, Zod",
            "HTML sanitizers",
            "RBAC systems",
            "TLS, AES encryption",
            "Structured logging",
            "Redis, rate limiting"
        ]
    }
    
    df_security = pd.DataFrame(security_aspects)
    st.dataframe(df_security, use_container_width=True)

def show_hands_on_exercises():
    """Display hands-on exercises and practice problems"""
    
    st.markdown('<h2 class="section-header">💪 Hands-On Exercises</h2>', unsafe_allow_html=True)
    
    # Exercise 1
    st.markdown('<h3 class="step-header">Exercise 1: Build a Simple Calculator Agent</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Create a basic agent that can perform mathematical calculations.
    
    **Requirements:**
    - Implement the ReACT pattern
    - Add calculator tools (add, subtract, multiply, divide)
    - Handle error cases (division by zero)
    - Test with various math problems
    """)
    
    st.markdown("**Starter Code:**")
    st.code("""
class CalculatorAgent:
    def __init__(self):
        # TODO: Initialize agent components
        self.tools = {}
        self.memory = []
    
    def run(self, math_problem: str):
        # TODO: Implement ReACT pattern
        # 1. Parse the math problem
        # 2. Choose appropriate tool
        # 3. Execute calculation
        # 4. Return result
        pass
    """, language="python")
    
    # Exercise 2
    st.markdown('<h3 class="step-header">Exercise 2: Create a Multi-Agent System</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Build a system with multiple specialized agents that collaborate.
    
    **Requirements:**
    - Create different agent types (researcher, analyzer, summarizer)
    - Implement communication between agents
    - Add coordination mechanism
    - Test with complex tasks
    """)
    
    # Exercise 3
    st.markdown('<h3 class="step-header">Exercise 3: Implement Memory and Learning</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Add memory and learning capabilities to an agent.
    
    **Requirements:**
    - Implement short-term and long-term memory
    - Add learning from experience
    - Test with repeated tasks
    - Measure improvement over time
    """)
    
    # Exercise 4
    st.markdown('<h3 class="step-header">Exercise 4: Build a Production-Ready Agent</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Create a production-ready agent with monitoring and error handling.
    
    **Requirements:**
    - Add comprehensive error handling
    - Implement monitoring and metrics
    - Add health checks
    - Test under load
    - Deploy and monitor
    """)
    
    # Interactive Code Editor
    st.markdown('<h3 class="step-header">Interactive Code Editor</h3>', unsafe_allow_html=True)
    
    st.markdown("**Try implementing your own agent here:**")
    
    # Simple code editor simulation
    code_input = st.text_area(
        "Write your agent code here:",
        height=300,
        placeholder="""class MyAgent:
    def __init__(self):
        # Your implementation here
        pass
    
    def run(self, task):
        # Your agent logic here
        pass"""
    )
    
    if st.button("Run Code"):
        st.success("Code executed! (This is a simulation)")
        st.code("Output: Agent created successfully!", language="text")
    
    # Progress Tracking
    st.markdown('<h3 class="step-header">Learning Progress</h3>', unsafe_allow_html=True)
    
    progress_data = {
        "Exercise": ["Calculator Agent", "Multi-Agent System", "Memory & Learning", "Production Agent"],
        "Status": ["✅ Completed", "🔄 In Progress", "⏳ Not Started", "⏳ Not Started"],
        "Difficulty": ["Easy", "Medium", "Hard", "Expert"],
        "Time Estimate": ["2 hours", "4 hours", "6 hours", "8 hours"]
    }
    
    df_progress = pd.DataFrame(progress_data)
    st.dataframe(df_progress, use_container_width=True)
    
    # Tips and Resources
    st.markdown('<h3 class="step-header">Tips and Resources</h3>', unsafe_allow_html=True)
    
    tips = [
        "Start with simple agents and gradually add complexity",
        "Test your agents with edge cases and error scenarios",
        "Use proper logging and debugging techniques",
        "Document your agent's capabilities and limitations",
        "Consider performance implications of your design choices",
        "Implement proper error handling and recovery mechanisms",
        "Use version control and testing frameworks",
        "Monitor your agents in production environments"
    ]
    
    for i, tip in enumerate(tips, 1):
        st.markdown(f"**{i}.** {tip}")
