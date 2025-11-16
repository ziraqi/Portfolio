"""
BMW Sales Data Visualization Portfolio
Main application entry point
Author: Zakaria Iraqi
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Zakaria Iraqi - Data Viz Portfolio",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 2rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        text-align: center;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main page content
st.markdown('<p class="main-header">🚗 BMW Sales Analytics Portfolio</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Data Visualization Project by Zakaria Iraqi</p>', unsafe_allow_html=True)

st.markdown("---")

# Welcome section
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    ### Welcome to My Data Visualization Portfolio
    
    This interactive portfolio showcases my skills in data analysis and visualization using Python, 
    Streamlit, and modern data science tools. Explore BMW worldwide sales data (2010-2024) through 
    multiple interactive pages:
    
    **📄 Bio** - Learn about my background and visualization philosophy
    
    **📊 EDA Gallery** - Explore four different visualization types answering key business questions
    
    **📈 Dashboard** - Interactive dashboard with filters and real-time insights
    
    **🧭 Future Work** - Potential enhancements and next steps
    
    ---
    
    ### About This Project
    
    This project analyzes a comprehensive dataset of 50,000 BMW vehicle sales records from 2010 to 2024. 
    The analysis explores market trends, pricing strategies, model performance, and the impact of 
    electrification on BMW's sales across global regions.
    
    **Navigate using the sidebar** to explore different sections of this portfolio.
    """)

st.markdown("---")

# Quick stats section
st.subheader("📊 Dataset Quick Stats")

import pandas as pd

@st.cache_data
def load_data():
       try:
           return pd.read_csv('assets/BMWdata.csv')
       except FileNotFoundError:
           st.error("Data file not found! Please check assets/BMWdata.csv exists.")
           return None

try:
    df = load_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    
    with col2:
        st.metric("Years Covered", f"{df['Year'].min()}-{df['Year'].max()}")
    
    with col3:
        st.metric("BMW Models", df['Model'].nunique())
    
    with col4:
        st.metric("Global Regions", df['Region'].nunique())
        
except Exception as e:
    st.warning("Unable to load dataset preview. Please ensure the data file is in the correct location.")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>Built with Python, Streamlit, Pandas, and Plotly</p>
    <p>© 2025 Zakaria Iraqi | Metropolitan State University of Denver</p>
</div>
""", unsafe_allow_html=True)