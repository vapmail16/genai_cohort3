#!/usr/bin/env python3
"""
MCP Understanding - Interactive Tutorial
Run script for the Streamlit application
"""

import subprocess
import sys
import os

def main():
    """Run the MCP Understanding Streamlit app"""
    
    print("🔌 Starting MCP Understanding - Interactive Tutorial")
    print("=" * 60)
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit is not installed")
        print("Please install requirements: pip install -r requirements.txt")
        sys.exit(1)
    
    # Check if required files exist
    required_files = [
        "streamlit_app.py",
        "app_modules.py",
        "requirements.txt"
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Required file not found: {file}")
            sys.exit(1)
    
    print("✅ All required files found")
    
    # Run the Streamlit app
    try:
        print("\n🚀 Launching MCP Understanding Tutorial...")
        print("The app will open in your default web browser")
        print("Press Ctrl+C to stop the application")
        print("-" * 60)
        
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8503",
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false"
        ])
        
    except KeyboardInterrupt:
        print("\n\n👋 MCP Understanding Tutorial stopped")
        print("Thank you for using the tutorial!")
        
    except Exception as e:
        print(f"\n❌ Error running the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
