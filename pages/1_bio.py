"""
Bio Page - Professional Information
"""

import streamlit as st

st.set_page_config(page_title="Bio - Zakaria Iraqi", page_icon="📄", layout="wide")

# Header
st.title("📄 Professional Bio")
st.markdown("---")

# Main bio section
col1, col2 = st.columns([1, 2])

with col1:
    # Placeholder for profile image
    st.image("https://via.placeholder.com/300x300.png?text=Zakaria+Iraqi", 
             caption="Zakaria Iraqi - CS Student & Data Enthusiast",
             use_container_width=True)
    
    st.markdown("""
    ### 📧 Contact
    **Email:** zakaria.iraqi@gmail.com  
    **LinkedIn:** https://www.linkedin.com/in/zakaria-iraqi-1355b7272/  
    **GitHub:** https://github.com/ziraqi
    
    ### 🎓 Education
    **Metropolitan State University of Denver**  
    B.S. in Computer Science  
    Expected: December 2025
    """)

with col2:
    st.markdown("""
    ### About Me
    
    I'm Zakaria Iraqi, a Computer Science student at Metropolitan State University of Denver graduating 
    in December 2025. With nearly 4 years of experience at Nike as a Visual Merchandising Specialist 
    and recent completion of a Frontend Software Developer Internship at DeNovo Solutions, I combine 
    creative problem-solving with technical expertise.
    
    I'm passionate about leveraging technology to solve real-world problems, particularly in data 
    visualization and analysis. My current focus is on building accessible, insightful data products 
    that help stakeholders make informed decisions. I'm particularly interested in the intersection 
    of data science, frontend development, and user experience design.
    
    Beyond academics and work, I'm driven by a vision to improve technology access in developing 
    countries through innovative startup solutions. I believe data visualization plays a crucial role 
    in democratizing information and empowering communities.
    """)

st.markdown("---")

# Highlights section
st.subheader("✨ Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🎓 Academic Focus**
    - Data Visualization (CS-39AE)
    - Algorithms & Data Structures
    - Cybersecurity
    - Programming Languages Theory
    - Capstone: ML Drift Detection System
    """)

with col2:
    st.markdown("""
    **🛠️ Technical Skills**
    - **Languages:** Python, JavaScript, Java
    - **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly
    - **Frameworks:** React, Vite, Streamlit
    - **Tools:** Git, Tableau, Jupyter, VS Code
    - **Data:** SQL, CSV processing, API integration
    """)

with col3:
    st.markdown("""
    **💼 Professional Experience**
    - Frontend Developer Intern @ DeNovo Solutions
    - Visual Merchandising Specialist @ Nike (4 years)
    - Capstone Team Lead (Frontend, 4 members)
    - Scrum & Agile methodologies
    - Git branching strategies & workflows
    """)

st.markdown("---")

# Visualization Philosophy
st.subheader("🎨 My Visualization Philosophy")

st.markdown("""
I believe effective data visualization is built on three core principles:

**1. Clarity Above All**  
Visualizations should communicate insights immediately. I prioritize clean designs, clear labels, 
and intuitive layouts that reduce cognitive load. Every chart element should serve a purpose—if 
it doesn't help tell the story, it doesn't belong.

**2. Accessibility & Inclusivity**  
Data should be accessible to everyone, regardless of visual abilities or technical background. 
I use colorblind-safe palettes, provide alternative text for screen readers, and include plain-language 
explanations. Good visualization democratizes information.

**3. Ethical Representation**  
With data comes responsibility. I'm committed to honest representations that avoid misleading scales, 
acknowledge limitations, and respect the privacy and dignity of individuals represented in datasets. 
I believe in transparency about data sources, methodologies, and potential biases.

These principles guide every visualization I create, from exploratory analysis to polished dashboards. 
Data visualization isn't just about making pretty charts—it's about empowering people with truthful, 
accessible insights they can act on.
""")

st.markdown("---")

# Current Projects
st.subheader("🚀 Current Projects")

st.markdown("""
**Drift Detection Monitoring System** (Capstone Project)  
Leading a team of four in developing a React + Vite application that monitors machine learning models 
for data drift. My role focuses on frontend architecture, UI/UX design, and team coordination through 
Git workflows and Scrum methodologies.

**Data Visualization Portfolio**  
Building this interactive Streamlit application to showcase data analysis skills through exploration 
of BMW worldwide sales data (2010-2024). The project demonstrates proficiency in Python data analysis 
libraries, interactive dashboard creation, and data storytelling.
""")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem 0;'>
    <p><em>"The goal is to turn data into information, and information into insight."</em> - Carly Fiorina</p>
</div>
""", unsafe_allow_html=True)