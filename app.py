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
st.markdown("""
<style>

.card{
    background:linear-gradient(145deg,#1e293b,#0f172a);
    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    padding:22px;
    box-shadow:0 8px 25px rgba(0,0,0,.30);
    transition:.3s;
    height:180px;
}

.card:hover{
    transform:translateY(-8px);
    border:1px solid #3b82f6;
    box-shadow:0 15px 40px rgba(59,130,246,.25);
}

.card-header{
    display:flex;
    align-items:center;
    gap:10px;
    color:#94a3b8;
    font-size:16px;
    font-weight:600;
}

.card-value{
    font-size:42px;
    font-weight:700;
    color:white;
    margin-top:25px;
}

.card-footer{
    color:#22c55e;
    margin-top:18px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)
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
def kpi_card(
    title,
    value,
    icon,
    subtitle="",
    color="#3B82F6"
):
    st.html(
        f"""<div class="card">
            <div class="card-header">
                <span>{icon}</span>
                <span>{title}</span>
            </div>

            <div class="card-value">
                {value}
            </div>

            <div class="card-footer">
                {subtitle}
            </div>
        </div>
        """)
with st.container(border=True):
    st.header("Key Performance Indicators")
    st.caption("Metrics derived from the loaded dataset.")
    st.divider()
    st.subheader("📊 Logistics Overview")
    st.divider()
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        kpi_card(
            title="📦 Total Shipments",
            value=f"{metrics['Total Shipments']:,}",
            icon="📦"
        )

    with c2:
        kpi_card(
            title="🚚 Avg Lead Time",
            value=f"{metrics['Average Lead Time']} Days",
            icon="🚚",
            subtitle="↓ -0.4 Days"
        )

    with c3:
        kpi_card(
            title="⚠ Delay Rate",
            value=f"{metrics['Delay Rate']}%",
            icon="⚠",
            subtitle="↓ -2.1%"
        )

    with c4:
        kpi_card(
            title="🌎 Regions Served",
            value=metrics["Regions Served"],
            icon="🌎"
        )
    st.divider()
    st.subheader("💰 Business Performance")
    st.divider()
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        kpi_card(
            title="💵 Total Sales",
            value=f"${metrics['Total Sales']:,.0f}",
            icon="💵"
        )

    with c2:
        kpi_card(
            title="📈 Gross Profit",
            value=f"${metrics['Gross Profit']:,.0f}",
            icon="📈"
        )

    with c3:
        kpi_card(
            title="📦 Units Sold",
            value=f"{metrics['Total Units']:,}",
            icon="📦"
        )

    with c4:
        kpi_card(
            title="👥 Customers",
            value=metrics["Unique Customers"],
            icon="👥"
        )
    st.divider()
    st.subheader("🚛 Shipping Insights")
    st.divider()
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        kpi_card(
            title="🚛 Ship Mode",
            value=metrics["Most Used Ship Mode"],
            icon="🚛"
        )   

    with c2:
        kpi_card(
            title="📍 States",
            value=metrics["States Served"],
            icon="📍"
        )

    with c3:
        kpi_card(
            title="🛒 Avg Order",
            value=f"${metrics['Average Order Value']:,.2f}",
            icon="🛒"
        )

    with c4:
        kpi_card(
            title="📅 Report",
            value="Live",
            icon="📅"
        )
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