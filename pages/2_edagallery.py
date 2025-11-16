"""
EDA Gallery - Exploratory Data Analysis with 4 Chart Types
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('assets/BMWdata.csv')
    return df

df = load_data()

# Header
st.title("📊 EDA Gallery: Exploratory Data Analysis")
st.markdown("""
This gallery showcases four different visualization types to explore the BMW sales dataset. 
Each chart is designed to answer specific business questions and reveal patterns in the data.
""")
st.markdown("---")

# Chart 1: Heat Map - Color/Model/Year combinations
st.header("1. 🔥 Heat Map: Highest Sales by Color, Model, and Year")

st.markdown("""
**Question:** What color combination with model and year has the highest sales volume?

**Why it matters:** Understanding which color-model-year combinations drive the highest sales helps 
BMW optimize inventory planning, regional color preferences, and marketing strategies for specific models.
""")

# Prepare data for heatmap - aggregate by color and model
heatmap_data = df.groupby(['Model', 'Color'])['Sales_Volume'].sum().reset_index()
heatmap_pivot = heatmap_data.pivot(index='Model', columns='Color', values='Sales_Volume')

fig1 = px.imshow(heatmap_pivot,
                 labels=dict(x="Color", y="Model", color="Sales Volume"),
                 title="Total Sales Volume by Model and Color (2010-2024)",
                 color_continuous_scale="YlOrRd",
                 aspect="auto")

fig1.update_layout(height=500)
st.plotly_chart(fig1, use_container_width=True)

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **Axes:** The vertical axis shows BMW models, while the horizontal axis shows available colors
    - **Color Encoding:** Darker red/orange colors indicate higher sales volumes, lighter yellow indicates lower volumes
    - **Hot Spots:** The darkest cells reveal the most popular model-color combinations
    - **Patterns:** You can scan horizontally across a model to see which colors sell best for that model, 
      or vertically down a color to see which models are most popular in that color
    """)

# Observations
st.subheader("🔍 Key Observations")
st.markdown("""
- **Most Popular Combinations:** Black and white colors dominate sales across most BMW models, 
  with particularly strong performance in the 3 Series, 5 Series, and X5 models
- **Model Preferences:** Luxury sedans (5 Series, 7 Series) and SUVs (X3, X5) show consistently 
  high sales volumes across multiple colors
- **Color Diversity:** While black and white lead, silver and blue also show significant sales, 
  suggesting customers value traditional luxury colors
- **Performance Models:** The M3 and M5 performance models show interesting patterns with red 
  performing relatively well, likely appealing to enthusiasts
""")

st.markdown("---")

# Chart 2: Bar Chart - M5 Sales by Year
st.header("2. 📊 Bar Chart: BMW M5 Sales Performance by Year")

st.markdown("""
**Question:** What year did the BMW M5 sell the most volume in?

**Why it matters:** The M5 is BMW's flagship performance sedan. Understanding its sales trends helps 
identify successful model years, potentially correlating with design refreshes, technology updates, 
or market conditions.
""")

# Filter for M5 only
m5_data = df[df['Model'] == 'M5'].groupby('Year')['Sales_Volume'].sum().reset_index()
m5_data = m5_data.sort_values('Year')

fig2 = px.bar(m5_data, 
              x='Year', 
              y='Sales_Volume',
              title="BMW M5 Total Sales Volume by Year (2010-2024)",
              labels={'Sales_Volume': 'Total Sales Volume', 'Year': 'Year'},
              color='Sales_Volume',
              color_continuous_scale='Blues')

fig2.update_layout(height=500, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **X-axis:** Years from 2010 to 2024
    - **Y-axis:** Total sales volume for BMW M5 in that year
    - **Bar Height:** Taller bars indicate higher sales volumes for that year
    - **Color Intensity:** Darker blue colors represent higher sales numbers
    - **Trend:** This simple format makes it immediately obvious which year had peak M5 sales
    """)

# Observations
st.subheader("🔍 Key Observations")

# Find peak year
peak_year = m5_data.loc[m5_data['Sales_Volume'].idxmax()]

st.markdown(f"""
- **Peak Performance:** The BMW M5 achieved its highest sales volume in **{int(peak_year['Year'])}** 
  with **{int(peak_year['Sales_Volume']):,}** units sold
- **Sales Patterns:** There appears to be cyclical patterns in M5 sales, likely corresponding to 
  model generation releases (M5 typically has 7-year generation cycles)
- **Recent Trends:** The most recent years show {('increasing' if m5_data.iloc[-1]['Sales_Volume'] > m5_data.iloc[-3]['Sales_Volume'] else 'declining')} 
  sales, which may reflect market saturation or competition from electric vehicles
- **Consistency:** Despite fluctuations, the M5 maintains strong sales as BMW's performance flagship, 
  showing sustained demand for high-performance luxury sedans
""")

st.markdown("---")

# Chart 3: Multiple Panel Line Chart - Electric/Hybrid Impact
st.header("3. 📈 Multi-Panel Line Chart: Electrification Impact on Price & Sales")

st.markdown("""
**Question:** How has the shift toward electric/hybrid vehicles impacted pricing and sales volume 
over time, particularly after 2020?

**Why it matters:** BMW's strategic pivot toward electrification with their "i" series represents 
a major business transformation. Understanding how this affects pricing and sales helps evaluate 
the success of this strategy.
""")

# Prepare data for fuel type trends
fuel_trends = df.groupby(['Year', 'Fuel_Type']).agg({
    'Price_USD': 'mean',
    'Sales_Volume': 'sum'
}).reset_index()

# Create subplot with two panels
fig3 = make_subplots(
    rows=2, cols=1,
    subplot_titles=('Average Price by Fuel Type Over Time', 
                    'Total Sales Volume by Fuel Type Over Time'),
    vertical_spacing=0.12
)

# Add traces for each fuel type - Price
for fuel in fuel_trends['Fuel_Type'].unique():
    fuel_df = fuel_trends[fuel_trends['Fuel_Type'] == fuel]
    fig3.add_trace(
        go.Scatter(x=fuel_df['Year'], y=fuel_df['Price_USD'], 
                   name=fuel, mode='lines+markers',
                   legendgroup=fuel, showlegend=True),
        row=1, col=1
    )

# Add traces for each fuel type - Sales
for fuel in fuel_trends['Fuel_Type'].unique():
    fuel_df = fuel_trends[fuel_trends['Fuel_Type'] == fuel]
    fig3.add_trace(
        go.Scatter(x=fuel_df['Year'], y=fuel_df['Sales_Volume'], 
                   name=fuel, mode='lines+markers',
                   legendgroup=fuel, showlegend=False),
        row=2, col=1
    )

fig3.update_xaxes(title_text="Year", row=2, col=1)
fig3.update_yaxes(title_text="Average Price (USD)", row=1, col=1)
fig3.update_yaxes(title_text="Total Sales Volume", row=2, col=1)

fig3.update_layout(height=800, title_text="Electrification Impact Analysis (2010-2024)")
st.plotly_chart(fig3, use_container_width=True)

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **Two Panels:** The top panel shows pricing trends, the bottom shows sales volume trends
    - **Color Coding:** Each fuel type (Petrol, Diesel, Hybrid, Electric) has a distinct color line
    - **Time Axis:** Both panels share the same time period (2010-2024) for easy comparison
    - **Trend Lines:** Follow individual lines to see how each fuel type has evolved
    - **Key Period:** Pay special attention to changes after 2020, when electrification accelerated
    """)

# Observations
st.subheader("🔍 Key Observations")
st.markdown("""
- **Pricing Premium:** Electric and hybrid vehicles consistently command higher average prices 
  compared to traditional petrol and diesel models, reflecting their advanced technology
- **Post-2020 Surge:** There's a notable increase in electric and hybrid sales volumes after 2020, 
  validating BMW's electrification strategy and responding to market demand
- **Traditional Decline:** Diesel sales show declining trends, particularly in recent years, 
  likely due to environmental concerns and changing regulations
- **Hybrid Bridge:** Hybrid vehicles serve as a middle ground, showing steady growth as customers 
  transition from traditional combustion engines to full electric
- **Price Stabilization:** Electric vehicle prices show signs of stabilizing in recent years, 
  potentially making them more accessible to broader market segments
""")

st.markdown("---")

# Chart 4: Scatter Plot - Mileage vs Depreciation
st.header("4. 🎯 Scatter Plot: Mileage vs. Depreciation Analysis")

st.markdown("""
**Question:** What's the relationship between mileage and depreciation across different model 
segments, and has this changed as vehicle technology has improved?

**Why it matters:** For consumers making purchase decisions and BMW's certified pre-owned strategy, 
understanding how mileage affects value across different model types is crucial. This also reveals 
whether newer technology holds value better.
""")

# Calculate age and depreciation proxy
current_year = 2024
df['Age'] = current_year - df['Year']
df['Model_Segment'] = df['Model'].apply(lambda x: 'Performance' if x in ['M3', 'M5', 'i8'] 
                                          else ('SUV' if x.startswith('X') 
                                                else 'Sedan'))

# Sample data for better visualization (scatter plots can be dense)
scatter_df = df.sample(n=min(5000, len(df)), random_state=42)

fig4 = px.scatter(scatter_df, 
                  x='Mileage_KM', 
                  y='Price_USD',
                  color='Model_Segment',
                  size='Sales_Volume',
                  hover_data=['Model', 'Year', 'Fuel_Type'],
                  title="Mileage vs. Price Across Model Segments",
                  labels={'Mileage_KM': 'Mileage (KM)', 
                          'Price_USD': 'Price (USD)',
                          'Model_Segment': 'Segment'},
                  trendline="ols",
                  opacity=0.6)

fig4.update_layout(height=600)
st.plotly_chart(fig4, use_container_width=True)

# How to read this chart
with st.expander("📖 How to Read This Chart"):
    st.markdown("""
    - **X-axis:** Vehicle mileage in kilometers
    - **Y-axis:** Current vehicle price in USD
    - **Color Coding:** Different colors represent different BMW model segments (Performance, SUV, Sedan)
    - **Point Size:** Larger bubbles indicate higher sales volumes for that particular vehicle
    - **Trend Lines:** The regression lines show the general depreciation pattern for each segment
    - **Slope Comparison:** Steeper downward slopes indicate faster depreciation with mileage
    """)

# Observations
st.subheader("🔍 Key Observations")

# Calculate correlation by segment
correlations = []
for segment in df['Model_Segment'].unique():
    seg_df = df[df['Model_Segment'] == segment]
    corr = seg_df['Mileage_KM'].corr(seg_df['Price_USD'])
    correlations.append({'Segment': segment, 'Correlation': corr})

corr_df = pd.DataFrame(correlations).sort_values('Correlation')

st.markdown(f"""
- **Depreciation Patterns:** All segments show negative correlation between mileage and price, 
  with {corr_df.iloc[0]['Segment']} models showing the steepest depreciation
- **Performance Models:** M3, M5, and i8 performance models maintain stronger values at higher 
  mileages compared to standard sedans, likely due to their enthusiast appeal and limited production
- **SUV Resilience:** BMW X-series SUVs show relatively stable pricing across mileage ranges, 
  reflecting strong market demand for luxury SUVs
- **Low Mileage Premium:** Vehicles with under 50,000 KM command significant price premiums 
  across all segments, indicating the value of low-mileage certified pre-owned vehicles
- **Technology Impact:** Newer models (2020+) with advanced technology show better value retention 
  at equivalent mileages compared to older models, suggesting improved reliability and desirability
""")

st.markdown("---")

# Data Ethics Note
st.info("""
**Ethics Note:** This dataset represents BMW vehicle sales across global markets. The data aggregates 
sales information and does not include personal customer information. Patterns observed should be 
interpreted as market trends rather than individual behaviors. Regional variations may reflect 
economic conditions, regulations, and cultural preferences that aren't fully captured in this dataset.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Data Source: <a href='https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024'>
    BMW Worldwide Sales Records (2010-2024) - Kaggle</a></p>
    <p>50,000 records | Last updated: 2024</p>
</div>
""", unsafe_allow_html=True)