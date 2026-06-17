import pandas as pd
from sales_analysis import SalesAnalyzer

def generate_dashboard():

    df = pd.read_csv(
        "data/processed_sales_data.csv"
    )

    analyzer = SalesAnalyzer(df)

    summary = (
        analyzer.generate_summary()
    )

    print("\n")
    print("=" * 50)
    print(
        "SALES DATA ANALYSIS DASHBOARD"
    )
    print("=" * 50)

    print(
        f"Total Revenue: ₹{summary['Total Revenue']}"
    )

    print(
        f"Total Orders: {summary['Total Orders']}"
    )

    print(
        f"Average Order Value: ₹{summary['Average Order Value']}"
    )

    print(
        f"Top Selling Product: {summary['Top Selling Product']}"
    )

    print("=" * 50)

    report_path = (
        "reports/sales_summary_report.txt"
    )

    with open(
        report_path,
        "w"
    ) as report:

        report.write(
            "SALES SUMMARY REPORT\n"
        )

        report.write(
            "=" * 50
        )

        report.write("\n\n")

        report.write(
            f"Total Revenue: ₹{summary['Total Revenue']}\n"
        )

        report.write(
            f"Total Orders: {summary['Total Orders']}\n"
        )

        report.write(
            f"Average Order Value: ₹{summary['Average Order Value']}\n"
        )

        report.write(
            f"Top Selling Product: {summary['Top Selling Product']}\n"
        )

        report.write(
            "\nBusiness Insights\n"
        )

        report.write(
            "-" * 50
        )

        report.write(
            "\n1. Sales performance analyzed successfully."
        )

        report.write(
            "\n2. Revenue trends evaluated."
        )

        report.write(
            "\n3. Product performance measured."
        )

        report.write(
            "\n4. Business KPIs generated."
        )

        report.write(
            "\n5. Data processing completed."
        )

    print(
        "\nReport generated successfully."
    )

    print(
        f"\nSaved at: {report_path}"
    )

if __name__ == "__main__":

    generate_dashboard()