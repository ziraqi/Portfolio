"""
Dashboard Page - Interactive BMW Sales Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('assets/BMWdata.csv')
    return df

df = load_data()

# Header
st.title("📈 BMW Sales Dashboard")
st.markdown("Interactive dashboard with real-time filtering and key performance indicators")
st.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Year range filter
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df['Year'].min()),
    max_value=int(df['Year'].max()),
    value=(int(df['Year'].min()), int(df['Year'].max()))
)

# Model multiselect
models = st.sidebar.multiselect(
    "Select BMW Models",
    options=sorted(df['Model'].unique()),
    default=sorted(df['Model'].unique())
)

# Region multiselect
regions = st.sidebar.multiselect(
    "Select Regions",
    options=sorted(df['Region'].unique()),
    default=sorted(df['Region'].unique())
)

# Fuel type filter
fuel_types = st.sidebar.multiselect(
    "Select Fuel Types",
    options=sorted(df['Fuel_Type'].unique()),
    default=sorted(df['Fuel_Type'].unique())
)

# Price range filter
price_range = st.sidebar.slider(
    "Price Range (USD)",
    min_value=int(df['Price_USD'].min()),
    max_value=int(df['Price_USD'].max()),
    value=(int(df['Price_USD'].min()), int(df['Price_USD'].max())),
    step=1000
)

# Apply filters
filtered_df = df[
    (df['Year'] >= year_range[0]) & 
    (df['Year'] <= year_range[1]) &
    (df['Model'].isin(models)) &
    (df['Region'].isin(regions)) &
    (df['Fuel_Type'].isin(fuel_types)) &
    (df['Price_USD'] >= price_range[0]) &
    (df['Price_USD'] <= price_range[1])
]

# Show active filters count
st.sidebar.markdown("---")
st.sidebar.metric("Filtered Records", f"{len(filtered_df):,} / {len(df):,}")

# KPI Section
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = filtered_df['Sales_Volume'].sum()
    st.metric(
        "Total Sales Volume",
        f"{total_sales:,.0f}",
        delta=f"{(total_sales/df['Sales_Volume'].sum()*100):.1f}% of total"
    )

with col2:
    avg_price = filtered_df['Price_USD'].mean()
    overall_avg = df['Price_USD'].mean()
    st.metric(
        "Average Price",
        f"${avg_price:,.0f}",
        delta=f"{((avg_price-overall_avg)/overall_avg*100):.1f}%"
    )

with col3:
    median_mileage = filtered_df['Mileage_KM'].median()
    st.metric(
        "Median Mileage",
        f"{median_mileage:,.0f} KM"
    )

with col4:
    unique_models = filtered_df['Model'].nunique()
    st.metric(
        "Active Models",
        f"{unique_models}"
    )

st.markdown("---")

# Visualizations
col1, col2 = st.columns(2)

with col1:
    # Sales by Region
    region_sales = filtered_df.groupby('Region')['Sales_Volume'].sum().reset_index()
    region_sales = region_sales.sort_values('Sales_Volume', ascending=True)
    
    fig1 = px.bar(region_sales, 
                  y='Region', 
                  x='Sales_Volume',
                  title="Sales Volume by Region",
                  labels={'Sales_Volume': 'Total Sales', 'Region': 'Region'},
                  orientation='h',
                  color='Sales_Volume',
                  color_continuous_scale='Blues')
    
    fig1.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Sales by Fuel Type
    fuel_sales = filtered_df.groupby('Fuel_Type')['Sales_Volume'].sum().reset_index()
    
    fig2 = px.pie(fuel_sales, 
                  values='Sales_Volume', 
                  names='Fuel_Type',
                  title="Sales Distribution by Fuel Type",
                  color_discrete_sequence=px.colors.qualitative.Set3)
    
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

# Full-width visualizations
st.markdown("---")

# Sales trend over time
sales_trend = filtered_df.groupby('Year').agg({
    'Sales_Volume': 'sum',
    'Price_USD': 'mean'
}).reset_index()

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=sales_trend['Year'],
    y=sales_trend['Sales_Volume'],
    mode='lines+markers',
    name='Sales Volume',
    line=dict(color='#1f77b4', width=3),
    marker=dict(size=8)
))

fig3.update_layout(
    title="Sales Volume Trend Over Time",
    xaxis_title="Year",
    yaxis_title="Total Sales Volume",
    height=400,
    hovermode='x unified'
)

st.plotly_chart(fig3, use_container_width=True)

# Model performance comparison
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    # Top models by sales
    model_sales = filtered_df.groupby('Model')['Sales_Volume'].sum().reset_index()
    model_sales = model_sales.sort_values('Sales_Volume', ascending=False).head(10)
    
    fig4 = px.bar(model_sales,
                  x='Sales_Volume',
                  y='Model',
                  title="Top 10 Models by Sales Volume",
                  orientation='h',
                  color='Sales_Volume',
                  color_continuous_scale='Viridis')
    
    fig4.update_layout(height=500, showlegend=False)
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    # Transmission distribution
    trans_data = filtered_df.groupby(['Transmission', 'Fuel_Type'])['Sales_Volume'].sum().reset_index()
    
    fig5 = px.sunburst(trans_data,
                       path=['Transmission', 'Fuel_Type'],
                       values='Sales_Volume',
                       title="Sales by Transmission & Fuel Type",
                       color='Sales_Volume',
                       color_continuous_scale='RdYlBu_r')
    
    fig5.update_layout(height=500)
    st.plotly_chart(fig5, use_container_width=True)

# Insights section
st.markdown("---")
st.subheader("💡 Key Insights")

insights_col1, insights_col2 = st.columns(2)

with insights_col1:
    st.markdown("""
    **Sales Performance**
    - The filtered dataset shows clear regional preferences, with some markets significantly 
      outperforming others
    - Seasonal patterns in sales volume may indicate optimal times for new model launches
    - The trend line reveals overall market direction and growth trajectory for BMW
    
    **Product Mix**
    - Fuel type distribution reflects BMW's transition toward electrification
    - Transmission preferences vary by region and model type
    - Performance models (M series) show distinct patterns compared to standard models
    """)

with insights_col2:
    st.markdown("""
    **Market Dynamics**
    - Price positioning varies significantly across regions and fuel types
    - Newer vehicle technologies command premium pricing but show strong sales volumes
    - The mileage-to-price ratio differs across model segments, impacting resale strategies
    
    **Strategic Considerations**
    - Regional customization opportunities based on color and feature preferences
    - Inventory optimization potential through better understanding of high-volume combinations
    - Pre-owned certification strategy can leverage depreciation patterns by segment
    """)

# Data limitations
st.info("""
**📌 Data Limitations & Context**

This dashboard analyzes 50,000 BMW sales records from 2010-2024. Please consider these limitations:

- **Temporal Scope:** Data may not capture the most recent 2-3 months of sales activity
- **Regional Aggregation:** Patterns reflect country/region-level trends, not city-specific preferences
- **External Factors:** Economic conditions, fuel prices, and regulations affect sales but aren't directly visible in this data
- **Selection Bias:** This dataset may over-represent certain markets or time periods based on data collection methods

**Best Use:** These insights are most valuable for identifying broad trends and patterns rather than making 
precise predictions about individual transactions or small market segments.
""")

# Reproducibility information
st.markdown("---")
st.markdown("""
**📁 Data Source:** [BMW Worldwide Sales Records (2010-2024) - Kaggle](https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024)

**🔄 Last Refreshed:** {}

**📊 Total Records:** {:,}
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), len(df)))

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem 0;'>
    <p>Interactive Dashboard | Built with Streamlit & Plotly | © 2025 Zakaria Iraqi</p>
</div>
""", unsafe_allow_html=True)