import pandas as pd

class ShippingAnalysisEngine:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):

        self.df = pd.read_csv(self.data_path)

        self.df["Order Date"] = pd.to_datetime(
            self.df["Order Date"],
            dayfirst=True
        )

        self.df["Ship Date"] = pd.to_datetime(
            self.df["Ship Date"],
            dayfirst=True
        )

        # Create Lead Time
        self.df["Lead Time"] = (
            self.df["Ship Date"] -
            self.df["Order Date"]
        ).dt.days
        # -----------------------------
        # Factory Mapping
        # -----------------------------
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

        self.df["Factory"] = self.df["Product Name"].map(factory_map)

        self.df["Route"] = (
            self.df["Factory"] +
            " → " +
            self.df["State"]
        )
        max_days = self.df["Lead Time"].max()

        self.df["Efficiency Score"] = (
            (max_days - self.df["Lead Time"]) /
            max_days * 100
        ).round(2)

        return self.df



    def clean_data(self):
        """Placeholder for data cleaning."""
        if self.df is None:
            return None

        # Future:
        # - Convert dates
        # - Remove invalid rows
        # - Handle missing values

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
        )
    

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

    def get_dataframe(self):
        return self.df