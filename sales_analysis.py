import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/sales.csv")

print("\n========== SALES ANALYSIS ==========\n")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Region-wise Sales
print("\nRegion Wise Sales")
print(df.groupby("Region")["Sales"].sum())

# Category-wise Sales
print("\nCategory Wise Sales")
print(df.groupby("Category")["Sales"].sum())

# Top Products
print("\nTop Products")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

# Sales by Category Chart
df.groupby("Category")["Sales"].sum().plot(
    kind="bar",
    title="Sales by Category"
)

plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()