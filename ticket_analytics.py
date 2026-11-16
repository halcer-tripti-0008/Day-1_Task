
import pandas as pd


class TicketAnalytics:

    def __init__(self, df):
        self.df = df

    def analyze(self):
        report = {
            "tickets_by_priority": self.df["priority"].value_counts().to_dict(),

            "average_resolution_time_by_category":
                self.df.groupby("category")["resolution_time_hours"].mean().round(2).to_dict(),

            "average_customer_rating":
                round(self.df["customer_rating"].mean(), 2),

            "unresolved_tickets":
                int((self.df["status"].str.lower() != "resolved").sum()),

            "missing_values":
                self.df.isna().sum().to_dict()
        }

        return report
