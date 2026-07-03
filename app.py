import streamlit as st
from engine import ShippingAnalysisEngine
from streamlit_option_menu import option_menu
import plotly.express as px

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
    factory = st.multiselect(
        "🏭 Factory",
        options=sorted(df["Factory"].dropna().unique()),
        default=[]
    )

    # Region
    region = st.multiselect(
        "🌎 Region",
        options=sorted(df["Region"].dropna().unique()),
        default=[]
   )

    # State
    state = st.multiselect(
        "📍 State",
        options=sorted(df["State"].dropna().unique()),
        default=[]
    )

    # Ship Mode
    ship_mode = st.multiselect(
        "🚚 Ship Mode",
        options=sorted(df["Ship Mode"].dropna().unique()),
        default=[]
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
    subtitle="",
    color="#3B82F6"
):
    st.html(
        f"""<div class="card">
            <div class="card-header">
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
        )

    with c2:
        kpi_card(
            title="🚚 Avg Lead Time",
            value=f"{metrics['Average Lead Time']} Days",
            subtitle="↓ -0.4 Days"
        )

    with c3:
        kpi_card(
            title="⚠ Delay Rate",
            value=f"{metrics['Delay Rate']}%",
            subtitle="↓ -2.1%"
        )

    with c4:
        kpi_card(
            title="🌎 Regions Served",
            value=metrics["Regions Served"],
        )
    st.divider()
    st.subheader("💰 Business Performance")
    st.divider()
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        kpi_card(
            title="💵 Total Sales",
            value=f"${metrics['Total Sales']:,.0f}",
        )

    with c2:
        kpi_card(
            title="📈 Gross Profit",
            value=f"${metrics['Gross Profit']:,.0f}",
        )

    with c3:
        kpi_card(
            title="📦 Units Sold",
            value=f"{metrics['Total Units']:,}",
        )

    with c4:
        kpi_card(
            title="👥 Customers",
            value=metrics["Unique Customers"],
        )
    st.divider()
    st.subheader("🚛 Shipping Insights")
    st.divider()
    c1,c2,c3,c4 = st.columns(4)

    with c1:
        kpi_card(
            title="🚛 Ship Mode",
            value=metrics["Most Used Ship Mode"],
        )   

    with c2:
        kpi_card(
            title="📍 States",
            value=metrics["States Served"],
        )

    with c3:
        kpi_card(
            title="🛒 Avg Order",
            value=f"${metrics['Average Order Value']:,.2f}",
        )

    with c4:
        kpi_card(
            title="📅 Report",
            value="Live",
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
    trend = engine.shipment_trend()

    fig1 = px.line(
        trend,
        x="Order Date",
        y="Shipments",
        markers=True,
        template="plotly_dark"
    )

    fig1.update_traces(
        line=dict(width=4),
        marker=dict(size=8)
    )

    fig1.update_layout(
        title="📈 Daily Shipment Trend",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        hovermode="x unified",
        height=420,
        title_x=0.02
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        key="shipment_trend",
    )
    st.divider()
    left, right = st.columns(2)
    with left:
        top = engine.top_routes()

        fig2 = px.bar(
            top,
            x="Avg_Lead_Time",
            y="Route",
            orientation="h",
            text="Avg_Lead_Time",
            color="Avg_Lead_Time",
            template="plotly_dark"
        )

        fig2.update_layout(
            title="🏆 Top 10 Fastest Routes",
            yaxis=dict(categoryorder="total ascending"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=500,
            title_x=0.02
        )

        fig2.update_traces(
            texttemplate="%{text:.2f} Days",
            textposition="outside"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True,
            key="top-10",
        )
    with right:
        worst = engine.worst_routes()

        fig3 = px.bar(
            worst,
            x="Avg_Lead_Time",
            y="Route",
            orientation="h",
            text="Avg_Lead_Time",
            color="Avg_Lead_Time",
            template="plotly_dark"
        )

        fig3.update_layout(
            title="🐢 Top 10 Slowest Routes",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=500,
            title_x=0.02
        )

        fig3.update_traces(
            texttemplate="%{text:.2f} Days",
            textposition="outside"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True,
            key="worst10",
        )
    volume = engine.shipment_volume()

    fig = px.bar(
            volume,
            x="Shipments",
            y="Route",
            orientation="h",
            color="Shipments",
            text="Shipments",
            template="plotly_dark"
        )

    fig.update_layout(
            title="📦 Top Shipment Routes",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=500
        )

    st.plotly_chart(fig, use_container_width=True, key="shipment_volume")

    sales = engine.sales_profit()

    fig = px.bar(
        sales,
        x="Route",
        y=["Sales","Profit"],
        barmode="group",
        template="plotly_dark"
    )

    fig.update_layout(
        title="💰 Sales vs Profit",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True, key="sales_profit")

    scatter = engine.route_scatter()

    fig = px.scatter(
        scatter,
        x="Lead_Time",
        y="Sales",
        size="Shipments",
        color="Lead_Time",
        hover_name="Route",
        template="plotly_dark"
    )

    fig.update_layout(
        title="🚚 Route Efficiency",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=550
    )

    st.plotly_chart(fig, use_container_width=True, key="route_scatter")



# ----------------------------------------------------
# Geographic Analysis
# ----------------------------------------------------
with tab3:
    st.subheader("Geographic Analysis")
    col1,col2 = st.columns(2)
    with col1:
        region = engine.region_analysis()

        fig = px.bar(
            region,
            x="Region",
            y="Sales",
            color="Lead_Time",
            text="Sales",
            template="plotly_dark"
        )

        fig.update_layout(
            title="🌎 Regional Sales Performance",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True, key="region")
    with col2:
        state = engine.state_analysis()

        fig = px.bar(
            state.sort_values("Sales", ascending=False).head(15),
            x="Sales",
            y="State",
            orientation="h",
            color="Lead_Time",
            template="plotly_dark"
        )

        fig.update_layout(
            title="📍 Top States by Sales",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=550
        )

        st.plotly_chart(fig, use_container_width=True, key="state")

# ----------------------------------------------------
# Ship Mode
# ----------------------------------------------------
with tab4:
    st.subheader("Ship Mode Analysis")
    st.info("Coming Soon")

st.divider()

st.caption("Developed using Python, Pandas, Plotly, and Streamlit.")