import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import random
from datetime import datetime

# Import our custom modules
from app_modules import (
    show_mcp_fundamentals, show_mcp_architectures, show_mcp_apis,
    show_mcp_vs_alternatives, show_real_world_applications, show_performance_optimization
)

# Page configuration
st.set_page_config(
    page_title="MCP Understanding - Interactive Tutorial",
    page_icon="🔌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #2c3e50;
    }
    .metric-box {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .code-block {
        background-color: #f1f3f4;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        font-family: 'Courier New', monospace;
        overflow-x: auto;
    }
    .highlight-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff;
    }
    .stTabs [data-baseweb="tab-panel"] {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 0px 4px 4px 4px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🔌 MCP Understanding</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Interactive Tutorial on Model Context Protocol (MCP)</p>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Navigation")
st.sidebar.markdown("---")

# Main content tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏗️ Fundamentals", 
    "🏛️ Architectures", 
    "🔧 APIs & Examples", 
    "⚖️ MCP vs Alternatives", 
    "🌍 Real-World Apps", 
    "⚡ Performance"
])

with tab1:
    show_mcp_fundamentals()

with tab2:
    show_mcp_architectures()

with tab3:
    show_mcp_apis()

with tab4:
    show_mcp_vs_alternatives()

with tab5:
    show_real_world_applications()

with tab6:
    show_performance_optimization()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🔌 MCP Understanding - Interactive Tutorial</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
