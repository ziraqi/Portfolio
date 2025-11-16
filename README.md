# 🚗 BMW Sales Data Visualization Portfolio

An interactive multi-page Streamlit application showcasing data visualization and analysis skills through exploration of BMW worldwide sales data (2010-2024).

## 📋 Project Overview

This portfolio application analyzes 50,000 BMW vehicle sales records to uncover market trends, pricing strategies, and the impact of electrification on sales performance. Built as part of the Data Visualization course (CS-39AE) at Metropolitan State University of Denver.

**Live Demo:** [Your Streamlit Cloud URL here]

## 👨‍💻 Author

**Zakaria Iraqi**  
Computer Science Student | Metropolitan State University of Denver  
Expected Graduation: December 2025

- **LinkedIn:** https://www.linkedin.com/in/zakaria-iraqi-1355b7272/  
- **GitHub:** https://github.com/ziraqi
- **Email:** zakaria.iraqi@gmail.com

## 🗺️ App Navigation

The portfolio consists of four main pages:

### 1. 📄 Bio
Professional background, technical skills, and data visualization philosophy. Includes highlights from academic work and professional experience.

### 2. 📊 EDA Gallery
Exploratory data analysis featuring four different visualization types:
- **Heat Map:** Color-model-year combinations with highest sales volumes
- **Bar Chart:** BMW M5 sales performance by year
- **Multi-Panel Line Chart:** Electric/hybrid impact on pricing and sales
- **Scatter Plot:** Mileage vs. depreciation analysis across model segments

Each chart includes:
- Research question and business justification
- "How to Read This Chart" guide (2-4 bullets)
- 3-6 key observations and insights

### 3. 📈 Dashboard
Interactive dashboard with:
- **Filters:** Year range, models, regions, fuel types, price range
- **KPIs:** Total sales volume, average price, median mileage, active models
- **Linked Visualizations:** 6+ charts that update together based on filter selections
- **Insights Section:** Data-driven recommendations and limitations

### 4. 🧭 Future Work
Proposed enhancements and project reflections:
- Predictive analytics & forecasting
- Geographic visualization & mapping
- Advanced accessibility audit
- Real-time data integration
- A/B testing framework

## 📊 Dataset Information

**Source:** [BMW Worldwide Sales Records (2010-2024)](https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024)

**Records:** 50,000 sales transactions

**Features:**
- Model, Year, Region, Color
- Engine Size, Mileage, Transmission, Fuel Type
- Price (USD), Sales Volume, Sales Classification

**Time Period:** 2010-2024

### Data Preprocessing

The following preprocessing steps were applied:
- No missing values detected in the dataset
- All numeric fields validated for appropriate ranges
- Categorical variables standardized for consistency
- No imputation required

### Ethics Note

This dataset represents BMW vehicle sales across global markets and does not include personal customer information. The data aggregates sales information at the transaction level. Results should be interpreted as market trends rather than individual behaviors. Regional variations may reflect economic conditions, regulations, and cultural preferences not fully captured in the dataset.

## 🛠️ Requirements

### Python Version
Python 3.8 or higher

### Dependencies

```
streamlit==1.38.0
pandas==2.2.1
numpy==1.26.4
plotly==5.20.0
```

## 🚀 Installation & Setup

### Local Development

1. **Clone the repository:**
```bash
git clone [your-repo-url]
cd streamlit_portfolio
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
streamlit run app.py
```

5. **Access the app:**
Open your browser and navigate to `http://localhost:8501`

### Deployment on Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select the main file: `app.py`
5. Click "Deploy"

## 📁 Project Structure

```
streamlit_portfolio/
├── app.py                      # Main application entry point
├── pages/
│   ├── 1_📄_Bio.py            # Professional bio page
│   ├── 2_📊_EDA_Gallery.py    # Exploratory data analysis
│   ├── 3_📈_Dashboard.py      # Interactive dashboard
│   └── 4_🧭_Future_Work.py    # Future enhancements
├── data/
│   └── bmw_sales.csv          # BMW sales dataset
├── assets/                     # Images, logos (if any)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🎨 Features

### Accessibility
- ♿ Colorblind-safe palettes (tested with coblis.com)
- 📱 Responsive design for mobile devices
- 🎯 Clear axis labels and units
- 📖 Plain-language chart explanations
- ⌨️ Keyboard navigation support

### Interactivity
- 🔍 Multiple synchronized filters
- 📊 Interactive hover details on all charts
- 🔄 Real-time KPI updates
- 🎛️ Customizable date ranges and selections

### Performance
- ⚡ Data caching with `@st.cache_data`
- 📦 Efficient data loading and processing
- 🚀 Optimized for 50K+ row datasets

## 📸 Screenshots

[Add 1-3 screenshots of your key pages here]

## 🤖 AI Assistance Acknowledgment

This project utilized ChatGPT (GPT-4) for:
- Generating additional research questions during the 5E Data Questioning Cycle
- Brainstorming visualization type selections
- Code review and debugging assistance
- README structure recommendations

All final implementations, analyses, and insights are original work.

## 🔮 Future Enhancements

Planned improvements include:
1. **Predictive Analytics:** Time series forecasting and price prediction models
2. **Geographic Maps:** Interactive choropleth and heat maps by region
3. **Accessibility Audit:** WCAG 2.1 AA compliance
4. **Real-Time Data:** ETL pipeline for live data integration
5. **A/B Testing:** Visualization effectiveness experiments

## 📝 License

This project is created for educational purposes as part of coursework at Metropolitan State University of Denver.

Dataset source: [Ahmad Raza Kashif on Kaggle](https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024)

## 🙏 Acknowledgments

- **Professor:** [Your professor's name] - CS-39AE Data Visualization
- **Institution:** Metropolitan State University of Denver
- **Dataset:** Ahmad Raza Kashif (Kaggle)
- **Tools:** Streamlit, Plotly, Pandas development teams

## 📧 Contact

For questions, feedback, or collaboration opportunities:
- **Email:** [Your email]
- **LinkedIn:** [Your LinkedIn]
- **Portfolio:** [This Streamlit App URL]

---

**Built with ❤️ using Python, Streamlit, and Plotly**

© 2024 Zakaria Iraqi | Metropolitan State University of Denver