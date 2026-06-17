import pandas as pd

class DataCleaner:

    def __init__(
        self,
        file_path
    ):

        self.file_path = file_path

    def load_data(self):

        return pd.read_csv(
            self.file_path
        )

    def remove_duplicates(
        self,
        dataframe
    ):

        return dataframe.drop_duplicates()

    def handle_missing_values(
        self,
        dataframe
    ):

        return dataframe.fillna(0)

    def standardize_columns(
        self,
        dataframe
    ):

        dataframe.columns = [
            col.strip().replace(
                " ",
                "_"
            )
            for col in dataframe.columns
        ]

        return dataframe

    def clean_data(self):

        df = self.load_data()

        df = self.remove_duplicates(df)

        df = self.handle_missing_values(df)

        df = self.standardize_columns(df)

        return df

if __name__ == "__main__":

    cleaner = DataCleaner(
        "data/sales_data.csv"
    )

    cleaned_data = (
        cleaner.clean_data()
    )

    cleaned_data.to_csv(
        "data/processed_sales_data.csv",
        index=False
    )

    print(
        "Data cleaning completed."
    )