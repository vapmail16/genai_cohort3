import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math
import random
from datetime import datetime
import json

# Import our custom modules
from app_modules import (
    show_ai_agent_fundamentals, show_agent_architectures, show_implementation_patterns,
    show_advanced_techniques, show_production_considerations, show_hands_on_exercises
)

# Page configuration
st.set_page_config(
    page_title="AI Agents Deep Dive - Step-by-Step Learning",
    page_icon="🤖",
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
    .step-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        color: #e74c3c;
        border-left: 4px solid #e74c3c;
        padding-left: 1rem;
    }
    .code-block {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        font-family: 'Courier New', monospace;
        overflow-x: auto;
        margin: 1rem 0;
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
    .exercise-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 2px solid #4169e1;
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
st.markdown('<h1 class="main-header">🤖 AI Agents Deep Dive</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Step-by-Step Learning: From Concepts to Production</p>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Learning Path")
st.sidebar.markdown("---")

# Progress tracking
if 'learning_progress' not in st.session_state:
    st.session_state.learning_progress = {
        'fundamentals': False,
        'architectures': False,
        'implementation': False,
        'advanced': False,
        'production': False,
        'exercises': False
    }

# Main content tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏗️ Fundamentals", 
    "🏛️ Architectures", 
    "⚙️ Implementation", 
    "🚀 Advanced", 
    "🏭 Production", 
    "💪 Exercises"
])

with tab1:
    show_ai_agent_fundamentals()

with tab2:
    show_agent_architectures()

with tab3:
    show_implementation_patterns()

with tab4:
    show_advanced_techniques()

with tab5:
    show_production_considerations()

with tab6:
    show_hands_on_exercises()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🤖 AI Agents Deep Dive - Step-by-Step Learning</p>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
