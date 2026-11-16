
import pandas as pd


class TicketDataProcessor:

    REQUIRED_COLUMNS = [
        "ticket_id",
        "category",
        "priority",
        "description",
        "resolution_time_hours",
        "customer_rating",
        "status"
    ]

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cleaned_df = None
        self.duplicate_count = 0
        self.missing_report = {}
        self.invalid_report = {}

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("CSV loaded successfully!")
            return self.df

        except FileNotFoundError:
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        except pd.errors.EmptyDataError:
            raise ValueError("The CSV file is empty.")

        except pd.errors.ParserError:
            raise ValueError("Invalid CSV format.")

    def validate_columns(self):
        if self.df is None:
            raise ValueError("Please load the CSV first.")

        missing_columns = [
            col for col in self.REQUIRED_COLUMNS
            if col not in self.df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        print("Column validation successful!")
        return True

    def handle_duplicates(self):
        if self.df is None:
            raise ValueError("Please load the CSV first.")

        self.duplicate_count = int(
            self.df["ticket_id"].duplicated().sum()
        )

        self.df = self.df.drop_duplicates(
            subset=["ticket_id"],
            keep="first"
        ).copy()

        return self.df

    def clean_data(self):
        self.validate_columns()

        self.cleaned_df = self.df.copy()

        self.missing_report = (
            self.cleaned_df.isna().sum().to_dict()
        )

        missing_ids = int(
            self.cleaned_df["ticket_id"].isna().sum()
        )

        self.cleaned_df = self.cleaned_df.dropna(
            subset=["ticket_id"]
        ).copy()

        self.invalid_report["missing_ticket_ids_removed"] = missing_ids

        self.duplicate_count = int(
            self.cleaned_df["ticket_id"].duplicated().sum()
        )

        self.cleaned_df = self.cleaned_df.drop_duplicates(
            subset=["ticket_id"],
            keep="first"
        ).copy()

        numeric_columns = [
            "resolution_time_hours",
            "customer_rating"
        ]

        for col in numeric_columns:
            original = self.cleaned_df[col]

            converted = pd.to_numeric(
                original,
                errors="coerce"
            )

            invalid_mask = original.notna() & converted.isna()

            self.invalid_report[f"invalid_{col}"] = int(
                invalid_mask.sum()
            )

            self.cleaned_df[col] = converted

        negative_time = (
            self.cleaned_df["resolution_time_hours"] < 0
        )

        self.invalid_report["negative_resolution_time"] = int(
            negative_time.sum()
        )

        self.cleaned_df.loc[
            negative_time, "resolution_time_hours"
        ] = float("nan")

        invalid_rating = ~self.cleaned_df[
            "customer_rating"
        ].between(1, 5)

        self.invalid_report["invalid_customer_rating"] = int(
            invalid_rating.sum()
        )

        self.cleaned_df.loc[
            invalid_rating, "customer_rating"
        ] = float("nan")

        text_columns = [
            "category",
            "priority",
            "description",
            "status"
        ]

        for col in text_columns:
            self.cleaned_df[col] = (
                self.cleaned_df[col].fillna("Unknown")
            )

        for col in numeric_columns:
            median_value = self.cleaned_df[col].median()

            if pd.isna(median_value):
                median_value = (
                    0.0 if col == "resolution_time_hours" else 3.0
                )

            self.cleaned_df[col] = (
                self.cleaned_df[col].fillna(median_value)
            )

        print("Data cleaning completed successfully!")
        return self.cleaned_df

    def get_cleaned_data(self):
        if self.cleaned_df is None:
            raise ValueError("Please clean the data first.")

        return self.cleaned_df

    def show_report(self):
        if self.cleaned_df is None:
            raise ValueError("Please clean the data first.")

        print("\nMissing values before cleaning:")
        print(self.missing_report)

        print("\nDuplicate ticket IDs removed:")
        print(self.duplicate_count)

        print("\nInvalid values found:")
        print(self.invalid_report)

        print("\nRemaining missing values:")
        print(self.cleaned_df.isna().sum())
