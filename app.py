import streamlit as st
from engine import ShippingAnalysisEngine
from streamlit_option_menu import option_menu

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
with st.sidebar:
    st.header("Filters")
    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Dashboard",
            "Route Analysis",
            "Geographic Analysis",
            "Ship Mode",
            "Raw Dataset"
        ],
        icons=[
            "speedometer2",
            "signpost-split",
            "geo-alt",
            "truck",
            "table"
        ],
        menu_icon="boxes",
        default_index=0,
    )

    st.divider()

    st.subheader("🎛 Dashboard Filters")

    # Date Filter
    date_range = st.date_input(
        "Date Range",
        value=[]
    )

    # Factory
    factory = st.selectbox(
        "🏭 Factory",
        [
            "All",
            "Lot's O' Nuts",
            "Wicked Choccy's",
            "Sugar Shack",
            "Secret Factory",
            "The Other Factory"
        ]
    )

    # Region
    region = st.multiselect(
        "🌎 Region",
        [
            "East",
            "West",
            "Central",
            "South"
        ]
    )

    # State
    state = st.multiselect(
        "📍 State",
        []
    )

    # Ship Mode
    ship_mode = st.multiselect(
        "🚚 Ship Mode",
        [
            "Standard Class",
            "Second Class",
            "First Class",
            "Same Day"
        ]
    )

    # Lead Time
    lead_time = st.slider(
        "⏳ Lead Time (Days)",
        min_value=0,
        max_value=30,
        value=(0, 10)
    )

    st.divider()

    if st.button("🔄 Reset Filters", use_container_width=True):
        st.rerun()
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