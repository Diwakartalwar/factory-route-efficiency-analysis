import streamlit as st
import pandas as pd

@st.cache_data(show_spinner=False)
def load_data_cached(data_path):

    df = pd.read_csv(data_path)

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True
    )

    df["Lead Time"] = (
        df["Ship Date"] -
        df["Order Date"]
    ).dt.days

    factory_map = {
        "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
        "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
        "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
        "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
        "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
        "Laffy Taffy": "Sugar Shack",
        "SweeTARTS": "Sugar Shack",
        "Nerds": "Sugar Shack",
        "Fun Dip": "Sugar Shack",
        "Fizzy Lifting Drinks": "Sugar Shack",
        "Everlasting Gobstopper": "Secret Factory",
        "Hair Toffee": "The Other Factory",
        "Lickable Wallpaper": "Secret Factory",
        "Wonka Gum": "Secret Factory",
        "Kazookles": "The Other Factory"
    }

    df["Factory"] = df["Product Name"].map(factory_map)

    df["Route"] = (
        df["Factory"] +
        " → " +
        df["State"]
    )

    max_days = df["Lead Time"].max()

    df["Efficiency Score"] = (
        (max_days - df["Lead Time"])
        / max_days * 100
    ).round(2)

    return df

class ShippingAnalysisEngine:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        self.df = load_data_cached(self.data_path)
        return self.df
        
    def clean_data(self):

        if self.df is None:
            return None

        # Remove duplicate rows
        self.df.drop_duplicates(inplace=True)

        # Remove rows with missing important values
        self.df.dropna(
            subset=[
                "Order Date",
                "Ship Date",
                "Sales",
                "Gross Profit",
                "Units"
            ],
            inplace=True
        )

        # Remove negative values
        self.df = self.df[
            self.df["Sales"] >= 0
        ]

        self.df = self.df[
            self.df["Gross Profit"] >= 0
        ]

        self.df = self.df[
            self.df["Units"] > 0
        ]

        # Remove whitespace
        text_columns = [
            "Region",
            "State",
            "City",
            "Ship Mode",
            "Division",
            "Product Name"
        ]

        for col in text_columns:

            self.df[col] = (
                self.df[col]
                .astype(str)
                .str.strip()
            )

        # Reset index
        self.df.reset_index(
            drop=True,
            inplace=True
        )

        return self.df

    def calculate_metrics(self):
        if self.df is None:
            raise ValueError("Load the dataset first.")
        df = self.df

        metrics = {

            # Logistics KPIs
            "Total Shipments": len(df),

            "Average Lead Time": round(
                df["Lead Time"].mean(), 2
            ),

            "Delay Rate": round(
                (df["Lead Time"] > 5).mean() * 100,
                2
            ),

            "Regions Served": df["Region"].nunique(),

            "States Served": df["State"].nunique(),

            "Most Used Ship Mode": df["Ship Mode"].mode()[0],

            # Business KPIs
            "Total Sales": df["Sales"].sum(),

            "Gross Profit": df["Gross Profit"].sum(),

            "Total Units": df["Units"].sum(),

            "Unique Customers": df["Customer ID"].nunique(),

            "Average Order Value": round(
                df["Sales"].mean(), 2
            )

        }

        return metrics
    
    def route_statistics(self):

        route_df = (
            self.df
            .groupby("Route")
            .agg(
                Shipments=("Order ID", "count"),
                Average_Lead_Time=("Lead Time", "mean"),
                Total_Sales=("Sales", "sum"),
                Total_Profit=("Gross Profit", "sum"),
                Units=("Units", "sum")
            )
            .reset_index()
        )

        route_df["Average_Lead_Time"] = (
            route_df["Average_Lead_Time"]
            .round(2)
        )

        return route_df
    
    def top_routes(self, n=10):
        return (
            self.df
            .groupby("Route")
            .agg(
                Shipments=("Order ID","count"),
                Avg_Lead_Time=("Lead Time","mean")
            )
            .sort_values("Avg_Lead_Time")
            .head(n)
            .reset_index()
        )
    
    def worst_routes(self, n=10):
        return (
            self.df
            .groupby("Route")
            .agg(
                Shipments=("Order ID","count"),
                Avg_Lead_Time=("Lead Time","mean")
            )
            .sort_values("Avg_Lead_Time", ascending=False)
            .head(n)
            .reset_index()
        )
    
    def shipment_trend(self):

        trend = (
            self.df
            .groupby("Order Date")
            .agg(
                Shipments=("Order ID","count"),
                Sales=("Sales","sum")
            )
            .reset_index()
        )

        return trend
    def get_filtered_data(
        self,
        factory=None,
        region=None,
        state=None,
        ship_mode=None
    ):

        df = self.df.copy()

        if factory:
            df = df[df["Factory"].isin(factory)]

        if region:
            df = df[df["Region"].isin(region)]

        if state:
            df = df[df["State/Province"].isin(state)]

        if ship_mode:
            df = df[df["Ship Mode"].isin(ship_mode)]

        return df


    def shipment_volume(self):

        return (
            self.df
            .groupby("Route")
            .agg(
                Shipments=("Order ID", "count")
            )
            .sort_values("Shipments", ascending=False)
            .head(10)
            .reset_index()
        )
    
    def sales_profit(self):

        return (
            self.df
            .groupby("Route")
            .agg(
                Sales=("Sales","sum"),
                Profit=("Gross Profit","sum")
            )
            .sort_values("Sales", ascending=False)
            .head(10)
            .reset_index()
        )
    def route_scatter(self):

        return (
        self.df
        .groupby("Route")
        .agg(
            Sales=("Sales","sum"),
            Lead_Time=("Lead Time","mean"),
            Shipments=("Order ID","count")
        )
        .reset_index()
        )
    
    def region_analysis(self):

        return (
        self.df
        .groupby("Region")
        .agg(
            Sales=("Sales","sum"),
            Profit=("Gross Profit","sum"),
            Shipments=("Order ID","count"),
            Lead_Time=("Lead Time","mean")
        )
        .reset_index()
        )
    def state_analysis(self):

        return (
        self.df
        .groupby("State")
        .agg(
            Sales=("Sales","sum"),
            Shipments=("Order ID","count"),
            Lead_Time=("Lead Time","mean")
        )
        .reset_index()
        )
    def region_distribution(self):
        return (
            self.df
            .groupby("Region")
            .size()
            .reset_index(name="Shipments")
        )
    def shipmode_analysis(self):

        return (
            self.df
            .groupby("Ship Mode")
            .agg(
                Shipments=("Order ID","count"),
                Sales=("Sales","sum"),
                Profit=("Gross Profit","sum"),
                Lead_Time=("Lead Time","mean"),
                Units=("Units","sum")
            )
            .reset_index()
        )
    
    def get_dataframe(self):
        return self.df