import csv

sales = [
    {"product": "Laptop", "quantity": 10, "price_per_unit": 1800},
    {"product": "Mobile", "quantity": 25, "price_per_unit": 1200},
    {"product": "Earpods", "quantity": 35, "price_per_unit": 250},
    {"product": "Watch", "quantity": 5, "price_per_unit": 499},
    {"product": "GPS", "quantity": 2, "price_per_unit": 99},
    {"product": "Charger", "quantity": 48, "price_per_unit": 26.89}
]

for sale in sales:
    sale["total"] = sale["quantity"] * sale["price_per_unit"]

with open("sales.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["product", "quantity", "price_per_unit", "total"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    writer.writerows(sales)

try:
    sales_from_csv = []

    with open("sales.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["price_per_unit"] = float(row["price_per_unit"])
            row["total"] = float(row["total"])
            sales_from_csv.append(row)
except FileNotFoundError:
    print("Sales.csv not found")
else:
    total_revenue = sum(sale["total"] for sale in sales_from_csv)
    average_order_value = total_revenue / len(sales_from_csv)
    best_sale = max(sales_from_csv, key=lambda sale: sale["total"])

    print(f"Total revenue: {total_revenue:,.2f}")
    print(f"Average order value: {average_order_value:,.2f}")
    print(f"Best selling product: {best_sale['product']} ({best_sale['total']:,.2f})")