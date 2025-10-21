import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import json
from datetime import datetime, timedelta

def show_mcp_fundamentals():
    """Display MCP fundamentals and core concepts"""
    
    st.markdown('<h2 class="section-header">🏗️ MCP Fundamentals</h2>', unsafe_allow_html=True)
    
    # What is MCP?
    st.markdown("### What is Model Context Protocol (MCP)?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Model Context Protocol (MCP)** is a standardized protocol that enables AI applications to securely connect to external data sources and tools. 
        It provides a structured way for AI models to interact with external systems through a well-defined interface.
        
        #### Key Characteristics:
        - **Standardized**: Consistent interface across different AI applications
        - **Secure**: Built-in security and authentication mechanisms
        - **Extensible**: Easy to add new tools and data sources
        - **Language Agnostic**: Works with any programming language
        - **Transport Flexible**: Supports multiple communication methods
        """)
    
    with col2:
        # MCP Logo/Icon representation
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white;">
            <h3>🔌 MCP</h3>
            <p>Model Context Protocol</p>
            <p style="font-size: 0.9rem;">Connecting AI to the World</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Core Components
    st.markdown("### 🧩 Core Components")
    
    components_data = {
        "Component": ["MCP Server", "MCP Client", "Transport Layer", "Tools", "Resources"],
        "Purpose": [
            "Exposes tools and resources to AI applications",
            "Connects to MCP servers and calls their tools", 
            "Handles communication between client and server",
            "Executable functions that perform specific tasks",
            "Data sources that can be read by AI applications"
        ],
        "Example": [
            "Billing system server",
            "AI assistant client",
            "HTTP, WebSocket, stdio",
            "create_invoice, send_email",
            "customer_data, invoice_history"
        ]
    }
    
    df_components = pd.DataFrame(components_data)
    st.dataframe(df_components, use_container_width=True)
    
    # MCP Message Flow
    st.markdown("### 📡 MCP Message Flow")
    
    # Create a visual representation of the message flow
    fig = go.Figure()
    
    # Add nodes
    nodes = [
        {"x": 0, "y": 0, "label": "AI Client", "color": "#667eea"},
        {"x": 2, "y": 0, "label": "MCP Server", "color": "#764ba2"},
        {"x": 4, "y": 0, "label": "External System", "color": "#28a745"}
    ]
    
    for i, node in enumerate(nodes):
        fig.add_trace(go.Scatter(
            x=[node["x"]], 
            y=[node["y"]], 
            mode='markers+text',
            marker=dict(size=50, color=node["color"]),
            text=node["label"],
            textposition="middle center",
            textfont=dict(color="white", size=12),
            name=node["label"],
            showlegend=False
        ))
    
    # Add arrows for message flow
    arrows = [
        {"x0": 0.3, "y0": 0, "x1": 1.7, "y1": 0, "label": "initialize"},
        {"x0": 1.7, "y0": 0, "x1": 0.3, "y1": 0, "label": "initialized"},
        {"x0": 0.3, "y0": -0.1, "x1": 1.7, "y1": -0.1, "label": "tools/list"},
        {"x0": 1.7, "y0": -0.1, "x1": 0.3, "y1": -0.1, "label": "tools/list result"},
        {"x0": 0.3, "y0": -0.2, "x1": 1.7, "y1": -0.2, "label": "tools/call"},
        {"x0": 1.7, "y0": -0.2, "x1": 0.3, "y1": -0.2, "label": "tools/call result"},
        {"x0": 2.3, "y0": 0, "x1": 3.7, "y1": 0, "label": "API calls"},
        {"x0": 3.7, "y0": 0, "x1": 2.3, "y1": 0, "label": "responses"}
    ]
    
    for arrow in arrows:
        fig.add_annotation(
            x=arrow["x1"], y=arrow["y1"],
            ax=arrow["x0"], ay=arrow["y0"],
            xref="x", yref="y",
            axref="x", ayref="y",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#666",
            text=arrow["label"],
            textangle=0,
            font=dict(size=10, color="#666")
        )
    
    fig.update_layout(
        title="MCP Communication Flow",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        showlegend=False,
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Transport Methods
    st.markdown("### 🚀 Transport Methods")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **stdio (Standard I/O)**
        - Process-to-process communication
        - Simple and reliable
        - Good for local development
        - Limited to single machine
        """)
    
    with col2:
        st.markdown("""
        **HTTP**
        - RESTful API communication
        - Works across networks
        - Stateless and scalable
        - Good for web applications
        """)
    
    with col3:
        st.markdown("""
        **WebSocket**
        - Real-time bidirectional communication
        - Persistent connections
        - Good for real-time applications
        - More complex to implement
        """)
    
    # Security Features
    st.markdown("### 🔒 Security Features")
    
    security_features = {
        "Feature": [
            "Authentication",
            "Authorization", 
            "Input Validation",
            "Rate Limiting",
            "Encryption",
            "Audit Logging"
        ],
        "Description": [
            "Verify client identity",
            "Control access to resources",
            "Validate all inputs",
            "Prevent abuse and overload",
            "Secure data transmission",
            "Track all operations"
        ],
        "Implementation": [
            "JWT tokens, API keys",
            "Role-based access control",
            "Schema validation",
            "Request throttling",
            "TLS/SSL encryption",
            "Comprehensive logging"
        ]
    }
    
    df_security = pd.DataFrame(security_features)
    st.dataframe(df_security, use_container_width=True)

def show_mcp_architectures():
    """Display different MCP architecture patterns"""
    
    st.markdown('<h2 class="section-header">🏛️ MCP Architectures</h2>', unsafe_allow_html=True)
    
    # Architecture Types
    st.markdown("### 🏗️ Common Architecture Patterns")
    
    # Single Server Architecture
    st.markdown("#### 1. Single Server Architecture")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Characteristics:**
        - One MCP server per domain
        - Simple to implement
        - Good for small applications
        - Limited scalability
        
        **Use Cases:**
        - Prototype development
        - Small business applications
        - Learning and experimentation
        """)
    
    with col2:
        # Visual representation
        fig = go.Figure()
        
        # Add nodes
        fig.add_trace(go.Scatter(
            x=[0, 2, 4], 
            y=[0, 0, 0], 
            mode='markers+text',
            marker=dict(size=50, color=["#667eea", "#764ba2", "#28a745"]),
            text=["AI Client", "MCP Server", "Database"],
            textposition="middle center",
            textfont=dict(color="white", size=12),
            showlegend=False
        ))
        
        # Add connections
        fig.add_annotation(x=2, y=0, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        
        fig.update_layout(
            title="Single Server Architecture",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=200,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Microservices Architecture
    st.markdown("#### 2. Microservices Architecture")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Characteristics:**
        - Multiple specialized MCP servers
        - Each server handles one domain
        - High scalability and maintainability
        - Complex orchestration
        
        **Use Cases:**
        - Large enterprise applications
        - Multi-domain systems
        - High-availability requirements
        """)
    
    with col2:
        # Visual representation
        fig = go.Figure()
        
        # Add nodes
        nodes = [
            {"x": 0, "y": 0, "label": "AI Client", "color": "#667eea"},
            {"x": 2, "y": 1, "label": "Billing MCP", "color": "#764ba2"},
            {"x": 2, "y": 0, "label": "User MCP", "color": "#764ba2"},
            {"x": 2, "y": -1, "label": "Notification MCP", "color": "#764ba2"},
            {"x": 4, "y": 1, "label": "Billing DB", "color": "#28a745"},
            {"x": 4, "y": 0, "label": "User DB", "color": "#28a745"},
            {"x": 4, "y": -1, "label": "Notification DB", "color": "#28a745"}
        ]
        
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[node["x"]], 
                y=[node["y"]], 
                mode='markers+text',
                marker=dict(size=40, color=node["color"]),
                text=node["label"],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
        
        # Add connections
        for i in range(1, 4):
            fig.add_annotation(x=2, y=2-i, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
            fig.add_annotation(x=4, y=2-i, ax=2, ay=2-i, showarrow=True, arrowhead=2, arrowcolor="#666")
        
        fig.update_layout(
            title="Microservices Architecture",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Gateway Architecture
    st.markdown("#### 3. Gateway Architecture")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Characteristics:**
        - Central gateway manages all MCP servers
        - Single entry point for AI clients
        - Centralized authentication and routing
        - Load balancing and failover
        
        **Use Cases:**
        - Multi-tenant applications
        - Complex enterprise systems
        - API management requirements
        """)
    
    with col2:
        # Visual representation
        fig = go.Figure()
        
        # Add nodes
        nodes = [
            {"x": 0, "y": 0, "label": "AI Client", "color": "#667eea"},
            {"x": 2, "y": 0, "label": "MCP Gateway", "color": "#ff6b6b"},
            {"x": 4, "y": 1, "label": "Server A", "color": "#764ba2"},
            {"x": 4, "y": 0, "label": "Server B", "color": "#764ba2"},
            {"x": 4, "y": -1, "label": "Server C", "color": "#764ba2"}
        ]
        
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[node["x"]], 
                y=[node["y"]], 
                mode='markers+text',
                marker=dict(size=40, color=node["color"]),
                text=node["label"],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
        
        # Add connections
        fig.add_annotation(x=2, y=0, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        for i in range(3):
            fig.add_annotation(x=4, y=1-i, ax=2, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        
        fig.update_layout(
            title="Gateway Architecture",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Architecture Comparison
    st.markdown("### 📊 Architecture Comparison")
    
    comparison_data = {
        "Architecture": ["Single Server", "Microservices", "Gateway"],
        "Complexity": ["Low", "High", "Medium"],
        "Scalability": ["Low", "High", "High"],
        "Maintainability": ["High", "Medium", "High"],
        "Performance": ["High", "Medium", "Medium"],
        "Cost": ["Low", "High", "Medium"],
        "Best For": [
            "Small projects, prototypes",
            "Large enterprises, complex domains",
            "Multi-tenant, API management"
        ]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)

def show_mcp_apis():
    """Display MCP API examples and implementations"""
    
    st.markdown('<h2 class="section-header">🔧 MCP APIs & Examples</h2>', unsafe_allow_html=True)
    
    # API Overview
    st.markdown("### 📡 MCP API Overview")
    
    st.markdown("""
    MCP provides a standardized set of APIs that enable AI applications to interact with external systems. 
    The protocol defines specific message types and formats for different operations.
    """)
    
    # Core API Methods
    st.markdown("### 🛠️ Core API Methods")
    
    api_methods = {
        "Method": [
            "initialize",
            "initialized", 
            "tools/list",
            "tools/call",
            "resources/list",
            "resources/read",
            "notifications/initialized",
            "notifications/tools/list_changed"
        ],
        "Purpose": [
            "Initialize connection between client and server",
            "Confirm successful initialization",
            "Get list of available tools",
            "Execute a specific tool",
            "Get list of available resources",
            "Read data from a resource",
            "Notify about successful initialization",
            "Notify about tool list changes"
        ],
        "Direction": [
            "Client → Server",
            "Server → Client",
            "Client → Server",
            "Client → Server", 
            "Client → Server",
            "Client → Server",
            "Server → Client",
            "Server → Client"
        ]
    }
    
    df_api = pd.DataFrame(api_methods)
    st.dataframe(df_api, use_container_width=True)
    
    # Code Examples
    st.markdown("### 💻 Code Examples")
    
    # Initialize Example
    st.markdown("#### 1. Connection Initialization")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Client Side (JavaScript/TypeScript)**")
        st.code("""
// Initialize MCP client
const client = new Client({
  name: "my-ai-app",
  version: "1.0.0"
});

// Connect to server
await client.connect(transport);

// Initialize connection
const initResult = await client.request({
  method: "initialize",
  params: {
    protocolVersion: "2024-11-05",
    capabilities: {
      tools: {},
      resources: {}
    },
    clientInfo: {
      name: "my-ai-app",
      version: "1.0.0"
    }
  }
});

console.log("Initialized:", initResult);
        """, language="javascript")
    
    with col2:
        st.markdown("**Server Side (TypeScript)**")
        st.code("""
// MCP Server implementation
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({
  name: "billing-server",
  version: "1.0.0"
});

// Handle initialization
server.setRequestHandler("initialize", async (request) => {
  return {
    protocolVersion: "2024-11-05",
    capabilities: {
      tools: {
        listChanged: true
      },
      resources: {
        subscribe: true,
        listChanged: true
      }
    },
    serverInfo: {
      name: "billing-server",
      version: "1.0.0"
    }
  };
});
        """, language="javascript")
    
    # Tool Registration Example
    st.markdown("#### 2. Tool Registration and Usage")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Server: Register Tool**")
        st.code("""
// Register a billing tool
server.registerTool("create_invoice", {
  description: "Create a new invoice",
  inputSchema: {
    type: "object",
    properties: {
      amount: {
        type: "number",
        description: "Invoice amount"
      },
      currency: {
        type: "string",
        description: "Currency code (e.g., USD, EUR)"
      },
      customer_email: {
        type: "string",
        format: "email",
        description: "Customer email address"
      }
    },
    required: ["amount", "currency", "customer_email"]
  }
}, async (params) => {
  const { amount, currency, customer_email } = params;
  
  // Create invoice logic
  const invoice = {
    id: generateId(),
    amount,
    currency,
    customer_email,
    status: "draft",
    created_at: new Date().toISOString()
  };
  
  // Store invoice
  invoices.set(invoice.id, invoice);
  
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          success: true,
          invoice_id: invoice.id,
          message: "Invoice created successfully"
        })
      }
    ]
  };
});
        """, language="javascript")
    
    with col2:
        st.markdown("**Client: Use Tool**")
        st.code("""
// List available tools
const toolsResult = await client.request({
  method: "tools/list"
});

console.log("Available tools:", toolsResult.tools);

// Call the create_invoice tool
const invoiceResult = await client.request({
  method: "tools/call",
  params: {
    name: "create_invoice",
    arguments: {
      amount: 150.00,
      currency: "USD",
      customer_email: "customer@example.com"
    }
  }
});

console.log("Invoice created:", invoiceResult);
        """, language="javascript")
    
    # Resource Access Example
    st.markdown("#### 3. Resource Access")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Server: Define Resource**")
        st.code("""
// Register a resource
server.registerResource("customer_data", {
  description: "Customer information",
  mimeType: "application/json"
}, async (uri) => {
  const customerId = uri.path.split('/').pop();
  const customer = customers.get(customerId);
  
  if (!customer) {
    throw new Error("Customer not found");
  }
  
  return {
    contents: [
      {
        uri: uri,
        mimeType: "application/json",
        text: JSON.stringify(customer)
      }
    ]
  };
});
        """, language="javascript")
    
    with col2:
        st.markdown("**Client: Access Resource**")
        st.code("""
// List available resources
const resourcesResult = await client.request({
  method: "resources/list"
});

console.log("Available resources:", resourcesResult.resources);

// Read customer data
const customerData = await client.request({
  method: "resources/read",
  params: {
    uri: "customer://123"
  }
});

console.log("Customer data:", customerData);
        """, language="javascript")
    
    # Error Handling
    st.markdown("#### 4. Error Handling")
    
    st.code("""
// Client-side error handling
try {
  const result = await client.request({
    method: "tools/call",
    params: {
      name: "create_invoice",
      arguments: invalidParams
    }
  });
} catch (error) {
  if (error.code === -32602) {
    console.error("Invalid parameters:", error.message);
  } else if (error.code === -32603) {
    console.error("Internal server error:", error.message);
  } else {
    console.error("Unknown error:", error);
  }
}

// Server-side error handling
server.registerTool("risky_operation", {
  description: "An operation that might fail",
  inputSchema: { /* ... */ }
}, async (params) => {
  try {
    // Perform risky operation
    const result = await performRiskyOperation(params);
    
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({ success: true, result })
        }
      ]
    };
  } catch (error) {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({ 
            success: false, 
            error: error.message 
          })
        }
      ],
      isError: true
    };
  }
});
    """, language="javascript")
    
    # Interactive Example
    st.markdown("### 🎮 Interactive MCP Example")
    
    st.markdown("Try out a simulated MCP interaction:")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("Initialize Connection", type="primary"):
            st.session_state.mcp_status = "Connected"
            st.success("✅ MCP connection initialized!")
    
    with col2:
        if st.button("List Tools"):
            if hasattr(st.session_state, 'mcp_status'):
                tools = ["create_invoice", "send_email", "get_customer", "update_billing"]
                st.write("Available tools:")
                for tool in tools:
                    st.write(f"• {tool}")
            else:
                st.warning("Please initialize connection first")
    
    with col3:
        if st.button("Call Tool"):
            if hasattr(st.session_state, 'mcp_status'):
                st.write("Tool called: create_invoice")
                st.write("Result: Invoice #12345 created successfully")
            else:
                st.warning("Please initialize connection first")

def show_mcp_vs_alternatives():
    """Display comparison between MCP and alternative protocols"""
    
    st.markdown('<h2 class="section-header">⚖️ MCP vs Alternatives</h2>', unsafe_allow_html=True)
    
    # Protocol Comparison
    st.markdown("### 🔄 Protocol Comparison")
    
    comparison_data = {
        "Feature": [
            "Standardization",
            "Security",
            "Real-time Support",
            "Language Support",
            "Learning Curve",
            "Community",
            "Documentation",
            "Enterprise Ready",
            "Performance",
            "Flexibility"
        ],
        "MCP": [
            "✅ High",
            "✅ Built-in",
            "✅ Yes",
            "✅ Multi-language",
            "🟡 Medium",
            "🟡 Growing",
            "✅ Good",
            "✅ Yes",
            "✅ High",
            "✅ High"
        ],
        "REST APIs": [
            "✅ High",
            "🟡 Manual",
            "❌ No",
            "✅ Multi-language",
            "✅ Easy",
            "✅ Large",
            "✅ Excellent",
            "✅ Yes",
            "🟡 Medium",
            "🟡 Medium"
        ],
        "GraphQL": [
            "✅ High",
            "🟡 Manual",
            "❌ No",
            "✅ Multi-language",
            "🟡 Medium",
            "✅ Large",
            "✅ Good",
            "✅ Yes",
            "🟡 Medium",
            "✅ High"
        ],
        "gRPC": [
            "✅ High",
            "✅ Built-in",
            "✅ Yes",
            "✅ Multi-language",
            "🟡 Medium",
            "✅ Large",
            "✅ Good",
            "✅ Yes",
            "✅ High",
            "🟡 Medium"
        ],
        "WebSockets": [
            "🟡 Medium",
            "🟡 Manual",
            "✅ Yes",
            "✅ Multi-language",
            "🟡 Medium",
            "✅ Large",
            "🟡 Medium",
            "🟡 Medium",
            "✅ High",
            "🟡 Medium"
        ]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True)
    
    # Detailed Comparison
    st.markdown("### 📊 Detailed Feature Analysis")
    
    # Create radar chart for comparison
    features = ['Standardization', 'Security', 'Real-time', 'Performance', 'Flexibility', 'Ease of Use']
    
    mcp_scores = [9, 9, 8, 9, 9, 7]
    rest_scores = [9, 6, 3, 6, 6, 9]
    graphql_scores = [9, 6, 3, 6, 8, 7]
    grpc_scores = [9, 9, 8, 9, 6, 6]
    websocket_scores = [6, 6, 9, 8, 6, 6]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=mcp_scores,
        theta=features,
        fill='toself',
        name='MCP',
        line_color='#667eea'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=rest_scores,
        theta=features,
        fill='toself',
        name='REST APIs',
        line_color='#28a745'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=graphql_scores,
        theta=features,
        fill='toself',
        name='GraphQL',
        line_color='#ff6b6b'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=grpc_scores,
        theta=features,
        fill='toself',
        name='gRPC',
        line_color='#ffc107'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=websocket_scores,
        theta=features,
        fill='toself',
        name='WebSockets',
        line_color='#6f42c1'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True,
        title="Protocol Feature Comparison (1-10 scale)"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Use Case Recommendations
    st.markdown("### 🎯 When to Use Each Protocol")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **✅ Use MCP when:**
        - Building AI-powered applications
        - Need standardized AI integration
        - Require real-time capabilities
        - Want built-in security features
        - Building microservices architecture
        - Need multi-language support
        """)
        
        st.markdown("""
        **✅ Use REST APIs when:**
        - Building traditional web applications
        - Need simple HTTP communication
        - Want maximum compatibility
        - Have existing REST infrastructure
        - Building public APIs
        - Need extensive documentation
        """)
    
    with col2:
        st.markdown("""
        **✅ Use GraphQL when:**
        - Need flexible data querying
        - Want to reduce over-fetching
        - Building mobile applications
        - Need real-time subscriptions
        - Want type-safe APIs
        - Building complex data relationships
        """)
        
        st.markdown("""
        **✅ Use gRPC when:**
        - Building high-performance services
        - Need strong typing
        - Want efficient serialization
        - Building microservices
        - Need streaming capabilities
        - Want language-agnostic contracts
        """)
    
    # Migration Strategies
    st.markdown("### 🔄 Migration Strategies")
    
    st.markdown("""
    #### From REST to MCP
    1. **Identify AI Integration Points**: Find where AI capabilities would add value
    2. **Create MCP Wrappers**: Wrap existing REST endpoints with MCP tools
    3. **Gradual Migration**: Start with non-critical endpoints
    4. **Update Clients**: Modify AI clients to use MCP instead of REST
    5. **Monitor Performance**: Ensure MCP doesn't impact existing functionality
    """)
    
    st.markdown("""
    #### From GraphQL to MCP
    1. **Map Queries to Tools**: Convert GraphQL queries to MCP tool calls
    2. **Preserve Type Safety**: Use MCP's schema validation
    3. **Handle Subscriptions**: Use MCP's notification system
    4. **Update Resolvers**: Convert GraphQL resolvers to MCP tools
    5. **Test Thoroughly**: Ensure all functionality is preserved
    """)
    
    # Performance Comparison
    st.markdown("### ⚡ Performance Comparison")
    
    # Generate sample performance data
    protocols = ['MCP', 'REST', 'GraphQL', 'gRPC', 'WebSocket']
    latency = [45, 60, 80, 35, 25]  # ms
    throughput = [850, 600, 400, 1200, 1000]  # requests/sec
    memory_usage = [120, 80, 150, 200, 100]  # MB
    
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=('Latency (ms)', 'Throughput (req/s)', 'Memory Usage (MB)'),
        specs=[[{"type": "bar"}, {"type": "bar"}, {"type": "bar"}]]
    )
    
    fig.add_trace(
        go.Bar(x=protocols, y=latency, name="Latency", marker_color='#667eea'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=protocols, y=throughput, name="Throughput", marker_color='#28a745'),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Bar(x=protocols, y=memory_usage, name="Memory", marker_color='#ff6b6b'),
        row=1, col=3
    )
    
    fig.update_layout(
        title="Performance Comparison",
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_real_world_applications():
    """Display real-world MCP applications and use cases"""
    
    st.markdown('<h2 class="section-header">🌍 Real-World Applications</h2>', unsafe_allow_html=True)
    
    # Application Categories
    st.markdown("### 🏢 Application Categories")
    
    categories = {
        "Category": [
            "E-commerce",
            "Healthcare", 
            "Finance",
            "Education",
            "Manufacturing",
            "Customer Service",
            "Content Management",
            "Data Analytics"
        ],
        "Use Cases": [
            "Product recommendations, inventory management, order processing",
            "Patient data analysis, treatment recommendations, appointment scheduling",
            "Fraud detection, risk assessment, automated trading",
            "Personalized learning, content generation, assessment",
            "Quality control, predictive maintenance, supply chain optimization",
            "Chatbots, ticket routing, knowledge base queries",
            "Content generation, SEO optimization, social media management",
            "Business intelligence, predictive analytics, reporting"
        ],
        "MCP Benefits": [
            "Personalized experiences, automated operations",
            "Improved patient outcomes, reduced errors",
            "Enhanced security, automated compliance",
            "Adaptive learning, efficient content creation",
            "Predictive insights, optimized operations",
            "24/7 support, consistent responses",
            "Automated content, improved engagement",
            "Real-time insights, data-driven decisions"
        ]
    }
    
    df_categories = pd.DataFrame(categories)
    st.dataframe(df_categories, use_container_width=True)
    
    # Detailed Use Cases
    st.markdown("### 💼 Detailed Use Cases")
    
    # E-commerce Example
    st.markdown("#### 🛒 E-commerce Platform")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **MCP Tools:**
        - `product_search`: Find products by description
        - `inventory_check`: Check product availability
        - `price_optimization`: Suggest optimal pricing
        - `recommendation_engine`: Generate product recommendations
        - `order_processing`: Handle order creation and updates
        - `customer_analysis`: Analyze customer behavior
        
        **AI Capabilities:**
        - Natural language product search
        - Personalized recommendations
        - Dynamic pricing optimization
        - Automated customer support
        - Fraud detection
        - Inventory forecasting
        """)
    
    with col2:
        # Create a flow diagram
        fig = go.Figure()
        
        # Add nodes
        nodes = [
            {"x": 0, "y": 0, "label": "Customer Query", "color": "#667eea"},
            {"x": 2, "y": 1, "label": "Product Search", "color": "#764ba2"},
            {"x": 2, "y": 0, "label": "Recommendation", "color": "#764ba2"},
            {"x": 2, "y": -1, "label": "Price Check", "color": "#764ba2"},
            {"x": 4, "y": 0, "label": "Order Processing", "color": "#28a745"}
        ]
        
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[node["x"]], 
                y=[node["y"]], 
                mode='markers+text',
                marker=dict(size=50, color=node["color"]),
                text=node["label"],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
        
        # Add connections
        fig.add_annotation(x=2, y=1, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=2, y=0, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=2, y=-1, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=1, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=-1, showarrow=True, arrowhead=2, arrowcolor="#666")
        
        fig.update_layout(
            title="E-commerce MCP Flow",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Healthcare Example
    st.markdown("#### 🏥 Healthcare System")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **MCP Tools:**
        - `patient_lookup`: Find patient records
        - `symptom_analysis`: Analyze symptoms and suggest diagnoses
        - `treatment_recommendation`: Suggest treatment options
        - `appointment_scheduling`: Schedule and manage appointments
        - `medication_check`: Check drug interactions
        - `lab_result_analysis`: Analyze lab results
        
        **AI Capabilities:**
        - Medical image analysis
        - Symptom pattern recognition
        - Treatment outcome prediction
        - Drug interaction detection
        - Automated documentation
        - Clinical decision support
        """)
    
    with col2:
        # Create a healthcare flow diagram
        fig = go.Figure()
        
        # Add nodes
        nodes = [
            {"x": 0, "y": 0, "label": "Patient Input", "color": "#667eea"},
            {"x": 2, "y": 1, "label": "Symptom Analysis", "color": "#764ba2"},
            {"x": 2, "y": 0, "label": "Record Lookup", "color": "#764ba2"},
            {"x": 2, "y": -1, "label": "Lab Analysis", "color": "#764ba2"},
            {"x": 4, "y": 0, "label": "Treatment Plan", "color": "#28a745"}
        ]
        
        for node in nodes:
            fig.add_trace(go.Scatter(
                x=[node["x"]], 
                y=[node["y"]], 
                mode='markers+text',
                marker=dict(size=50, color=node["color"]),
                text=node["label"],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
        
        # Add connections
        fig.add_annotation(x=2, y=1, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=2, y=0, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=2, y=-1, ax=0, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=1, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=0, showarrow=True, arrowhead=2, arrowcolor="#666")
        fig.add_annotation(x=4, y=0, ax=2, ay=-1, showarrow=True, arrowhead=2, arrowcolor="#666")
        
        fig.update_layout(
            title="Healthcare MCP Flow",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Implementation Examples
    st.markdown("### 🛠️ Implementation Examples")
    
    # Code Example
    st.markdown("#### E-commerce MCP Server")
    
    st.code("""
// E-commerce MCP Server
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({
  name: "ecommerce-server",
  version: "1.0.0"
});

// Product search tool
server.registerTool("product_search", {
  description: "Search for products using natural language",
  inputSchema: {
    type: "object",
    properties: {
      query: {
        type: "string",
        description: "Natural language product search query"
      },
      category: {
        type: "string",
        description: "Product category filter"
      },
      price_range: {
        type: "object",
        properties: {
          min: { type: "number" },
          max: { type: "number" }
        }
      }
    },
    required: ["query"]
  }
}, async (params) => {
  const { query, category, price_range } = params;
  
  // Use AI to understand the search query
  const searchTerms = await analyzeSearchQuery(query);
  
  // Search products in database
  const products = await searchProducts({
    terms: searchTerms,
    category,
    price_range
  });
  
  // Generate AI-powered recommendations
  const recommendations = await generateRecommendations(products);
  
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          products: products.slice(0, 10),
          recommendations,
          total_found: products.length
        })
      }
    ]
  };
});

// Inventory check tool
server.registerTool("inventory_check", {
  description: "Check product availability and stock levels",
  inputSchema: {
    type: "object",
    properties: {
      product_id: {
        type: "string",
        description: "Product identifier"
      },
      quantity: {
        type: "number",
        description: "Required quantity"
      }
    },
    required: ["product_id"]
  }
}, async (params) => {
  const { product_id, quantity = 1 } = params;
  
  const inventory = await checkInventory(product_id);
  const available = inventory.stock >= quantity;
  
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          product_id,
          available,
          stock_level: inventory.stock,
          requested_quantity: quantity,
          estimated_restock: inventory.restock_date
        })
      }
    ]
  };
});

// Start the server
server.start();
    """, language="javascript")
    
    # Success Stories
    st.markdown("### 🏆 Success Stories")
    
    success_stories = {
        "Company": [
            "TechCorp E-commerce",
            "HealthAI Systems",
            "FinanceFlow Inc",
            "EduTech Solutions",
            "ManufacturingAI"
        ],
        "Implementation": [
            "Product recommendation system",
            "Medical diagnosis assistant",
            "Fraud detection system",
            "Personalized learning platform",
            "Predictive maintenance system"
        ],
        "Results": [
            "35% increase in sales, 50% reduction in support tickets",
            "40% faster diagnosis, 25% reduction in errors",
            "60% reduction in fraud, 30% cost savings",
            "45% improvement in learning outcomes",
            "50% reduction in downtime, 20% cost savings"
        ],
        "MCP Benefits": [
            "Standardized AI integration, easy maintenance",
            "Secure patient data handling, compliance",
            "Real-time fraud detection, scalability",
            "Adaptive learning, personalized content",
            "Predictive insights, automated alerts"
        ]
    }
    
    df_success = pd.DataFrame(success_stories)
    st.dataframe(df_success, use_container_width=True)
    
    # Future Applications
    st.markdown("### 🚀 Future Applications")
    
    future_apps = [
        "**Smart Cities**: Traffic optimization, energy management, public safety",
        "**Autonomous Vehicles**: Real-time decision making, route optimization",
        "**Space Exploration**: Mission planning, data analysis, autonomous operations",
        "**Climate Change**: Environmental monitoring, carbon footprint tracking",
        "**Virtual Reality**: Immersive AI assistants, virtual world interactions",
        "**Quantum Computing**: Quantum algorithm optimization, error correction",
        "**Blockchain**: Smart contract automation, DeFi applications",
        "**IoT**: Device management, data processing, predictive maintenance"
    ]
    
    for app in future_apps:
        st.markdown(f"• {app}")

def show_performance_optimization():
    """Display performance optimization strategies and best practices"""
    
    st.markdown('<h2 class="section-header">⚡ Performance Optimization</h2>', unsafe_allow_html=True)
    
    # Performance Metrics
    st.markdown("### 📊 Key Performance Metrics")
    
    metrics_data = {
        "Metric": [
            "Response Time",
            "Throughput",
            "Latency",
            "Memory Usage",
            "CPU Usage",
            "Error Rate",
            "Availability",
            "Scalability"
        ],
        "Description": [
            "Time to complete a request",
            "Requests processed per second",
            "Network communication delay",
            "Memory consumption",
            "CPU utilization",
            "Percentage of failed requests",
            "System uptime percentage",
            "Ability to handle increased load"
        ],
        "Target": [
            "< 100ms",
            "> 1000 req/s",
            "< 50ms",
            "< 500MB",
            "< 70%",
            "< 0.1%",
            "> 99.9%",
            "Linear scaling"
        ],
        "Measurement": [
            "End-to-end timing",
            "Load testing",
            "Network monitoring",
            "Memory profiling",
            "CPU monitoring",
            "Error logging",
            "Uptime monitoring",
            "Load testing"
        ]
    }
    
    df_metrics = pd.DataFrame(metrics_data)
    st.dataframe(df_metrics, use_container_width=True)
    
    # Optimization Strategies
    st.markdown("### 🚀 Optimization Strategies")
    
    # Caching
    st.markdown("#### 1. Caching Strategies")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Client-Side Caching:**
        - Cache tool responses
        - Store resource data locally
        - Implement cache invalidation
        - Use appropriate TTL values
        
        **Server-Side Caching:**
        - Cache frequently accessed data
        - Use Redis or Memcached
        - Implement cache warming
        - Monitor cache hit rates
        """)
    
    with col2:
        # Cache performance chart
        cache_data = {
            "Cache Type": ["No Cache", "Memory Cache", "Redis Cache", "CDN Cache"],
            "Hit Rate": [0, 60, 85, 95],
            "Response Time": [200, 50, 30, 10]
        }
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=cache_data["Cache Type"],
            y=cache_data["Hit Rate"],
            name="Hit Rate (%)",
            marker_color='#667eea'
        ))
        fig.add_trace(go.Bar(
            x=cache_data["Cache Type"],
            y=cache_data["Response Time"],
            name="Response Time (ms)",
            marker_color='#28a745',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="Cache Performance Impact",
            xaxis_title="Cache Type",
            yaxis=dict(title="Hit Rate (%)", side="left"),
            yaxis2=dict(title="Response Time (ms)", side="right", overlaying="y"),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Connection Pooling
    st.markdown("#### 2. Connection Pooling")
    
    st.markdown("""
    **Benefits:**
    - Reuse existing connections
    - Reduce connection overhead
    - Improve response times
    - Better resource utilization
    
    **Implementation:**
    ```javascript
    // Connection pool configuration
    const poolConfig = {
      min: 5,        // Minimum connections
      max: 20,       // Maximum connections
      idle: 10000,   // Idle timeout (ms)
      acquire: 30000 // Acquire timeout (ms)
    };
    
    const pool = new Pool(poolConfig);
    ```
    """)
    
    # Load Balancing
    st.markdown("#### 3. Load Balancing")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Load Balancing Strategies:**
        - Round Robin
        - Least Connections
        - Weighted Round Robin
        - IP Hash
        - Geographic
        
        **Benefits:**
        - Distribute load evenly
        - Improve availability
        - Handle traffic spikes
        - Scale horizontally
        """)
    
    with col2:
        # Load balancing visualization
        fig = go.Figure()
        
        # Add load balancer
        fig.add_trace(go.Scatter(
            x=[0], y=[0], mode='markers+text',
            marker=dict(size=60, color='#ff6b6b'),
            text=['Load Balancer'],
            textposition="middle center",
            textfont=dict(color="white", size=12),
            showlegend=False
        ))
        
        # Add servers
        for i in range(3):
            fig.add_trace(go.Scatter(
                x=[2], y=[i-1], mode='markers+text',
                marker=dict(size=40, color='#28a745'),
                text=[f'Server {i+1}'],
                textposition="middle center",
                textfont=dict(color="white", size=10),
                showlegend=False
            ))
            
            # Add connection
            fig.add_annotation(
                x=2, y=i-1, ax=0, ay=0,
                showarrow=True, arrowhead=2, arrowcolor="#666"
            )
        
        fig.update_layout(
            title="Load Balancing Architecture",
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance Monitoring
    st.markdown("### 📈 Performance Monitoring")
    
    # Real-time metrics simulation
    st.markdown("#### Real-time Performance Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        response_time = random.randint(45, 120)
        st.metric("Response Time", f"{response_time}ms", f"{random.randint(-10, 10)}ms")
    
    with col2:
        throughput = random.randint(800, 1200)
        st.metric("Throughput", f"{throughput} req/s", f"{random.randint(-50, 50)} req/s")
    
    with col3:
        error_rate = random.uniform(0.01, 0.5)
        st.metric("Error Rate", f"{error_rate:.2f}%", f"{random.uniform(-0.1, 0.1):.2f}%")
    
    with col4:
        cpu_usage = random.randint(30, 80)
        st.metric("CPU Usage", f"{cpu_usage}%", f"{random.randint(-5, 5)}%")
    
    # Performance trends
    st.markdown("#### Performance Trends")
    
    # Generate sample data
    dates = pd.date_range(start='2024-01-01', end='2024-01-30', freq='D')
    response_times = [random.randint(40, 150) for _ in range(len(dates))]
    throughput_data = [random.randint(700, 1300) for _ in range(len(dates))]
    
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Response Time Over Time', 'Throughput Over Time'),
        vertical_spacing=0.1
    )
    
    fig.add_trace(
        go.Scatter(x=dates, y=response_times, name="Response Time", line=dict(color='#667eea')),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(x=dates, y=throughput_data, name="Throughput", line=dict(color='#28a745')),
        row=2, col=1
    )
    
    fig.update_layout(
        title="Performance Trends (30 Days)",
        height=600,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Best Practices
    st.markdown("### ✅ Best Practices")
    
    best_practices = {
        "Category": [
            "Code Optimization",
            "Database Optimization",
            "Network Optimization",
            "Monitoring",
            "Testing",
            "Deployment"
        ],
        "Practice": [
            "Use async/await, avoid blocking operations, implement proper error handling",
            "Use connection pooling, optimize queries, implement caching",
            "Use compression, minimize payload size, implement keep-alive",
            "Set up alerts, monitor key metrics, log important events",
            "Load testing, stress testing, performance testing",
            "Use CDNs, implement auto-scaling, optimize container images"
        ],
        "Impact": [
            "High",
            "High",
            "Medium",
            "High",
            "Medium",
            "Medium"
        ]
    }
    
    df_practices = pd.DataFrame(best_practices)
    st.dataframe(df_practices, use_container_width=True)
    
    # Performance Checklist
    st.markdown("### ✅ Performance Checklist")
    
    checklist_items = [
        "✅ Implement connection pooling",
        "✅ Add caching at multiple levels",
        "✅ Use async/await for I/O operations",
        "✅ Optimize database queries",
        "✅ Implement proper error handling",
        "✅ Set up performance monitoring",
        "✅ Use load balancing",
        "✅ Implement rate limiting",
        "✅ Optimize payload sizes",
        "✅ Use compression",
        "✅ Set up automated testing",
        "✅ Monitor memory usage",
        "✅ Implement graceful degradation",
        "✅ Use CDNs for static content",
        "✅ Implement auto-scaling"
    ]
    
    for item in checklist_items:
        st.markdown(item)
