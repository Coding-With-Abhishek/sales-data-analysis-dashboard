import pandas as pd

class SalesAnalyzer:

    def __init__(
        self,
        dataframe
    ):

        self.df = dataframe

    def total_revenue(self):

        return round(
            self.df[
                "Revenue"
            ].sum(),
            2
        )

    def total_orders(self):

        return len(self.df)

    def average_order_value(self):

        return round(
            self.df[
                "Revenue"
            ].mean(),
            2
        )

    def top_selling_product(self):

        return (
            self.df.groupby(
                "Product"
            )["Quantity"]
            .sum()
            .idxmax()
        )

    def category_sales(self):

        return (
            self.df.groupby(
                "Category"
            )["Revenue"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

    def monthly_sales(self):

        return (
            self.df.groupby(
                "Month"
            )["Revenue"]
            .sum()
        )

    def generate_summary(self):

        return {

            "Total Revenue":
            self.total_revenue(),

            "Total Orders":
            self.total_orders(),

            "Average Order Value":
            self.average_order_value(),

            "Top Selling Product":
            self.top_selling_product()
        }

if __name__ == "__main__":

    df = pd.read_csv(
        "data/processed_sales_data.csv"
    )

    analyzer = SalesAnalyzer(
        df
    )

    print(
        analyzer.generate_summary()
    )