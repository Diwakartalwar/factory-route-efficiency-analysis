import streamlit as st
from engine import ShippingAnalysisEngine

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Factory Route Efficiency Analysis",
    page_icon="🍬",
    layout="wide"
)

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.title("🍬 Factory-to-Customer Shipping Route Efficiency Analysis")
st.caption("Interactive logistics analytics dashboard for Nassau Candy Distributor.")

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------
engine = ShippingAnalysisEngine("data.csv")

try:
    df = engine.load_data()
    engine.clean_data()
    metrics = engine.calculate_metrics()

except Exception as e:
    st.error(f"Error loading dataset:\n{e}")
    st.stop()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
st.sidebar.header("Filters")

st.sidebar.info("Filters will be added here.")

# ----------------------------------------------------
# KPI Section
# ----------------------------------------------------
st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Orders", f"{metrics['Total Orders']:,}")
col2.metric("Sales", f"${metrics['Total Sales']:,.2f}")
col3.metric("Profit", f"${metrics['Total Profit']:,.2f}")
col4.metric("Avg Sales", f"${metrics['Average Sales']:.2f}")

st.divider()

# ----------------------------------------------------
# Tabs
# ----------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🚚 Route Analysis",
    "🗺 Geographic Analysis",
    "🚛 Ship Mode"
])

# ----------------------------------------------------
# Overview
# ----------------------------------------------------
with tab1:
    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

# ----------------------------------------------------
# Route Analysis
# ----------------------------------------------------
with tab2:
    st.subheader("Route Analysis")
    st.info("Coming Soon")

# ----------------------------------------------------
# Geographic Analysis
# ----------------------------------------------------
with tab3:
    st.subheader("Geographic Analysis")
    st.info("Coming Soon")

# ----------------------------------------------------
# Ship Mode
# ----------------------------------------------------
with tab4:
    st.subheader("Ship Mode Analysis")
    st.info("Coming Soon")

st.divider()

st.caption("Developed using Python, Pandas, Plotly, and Streamlit.")