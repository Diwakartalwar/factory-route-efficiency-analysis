import pandas as pd


class ShippingAnalysisEngine:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        """Load dataset."""
        self.df = pd.read_csv(self.data_path)
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
        """Placeholder for KPI calculations."""
        if self.df is None:
            return {}

        metrics = {
            "Total Orders": len(self.df),
            "Total Sales": self.df["Sales"].sum(),
            "Total Profit": self.df["Gross Profit"].sum(),
            "Average Sales": self.df["Sales"].mean(),
        }

        return metrics

    def get_dataframe(self):
        return self.df