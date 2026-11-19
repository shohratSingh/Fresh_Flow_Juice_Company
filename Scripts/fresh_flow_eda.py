import numpy as np
import csv

with open("D:\\PyCharm\\PyCharm_Files\\Fresh_Flow_Juice_Company\\DataSets\\freshflow_sales.csv", "r", newline="") as file:
    reader = csv.reader(file)


    headers = next(reader)


    rows = list(reader)


data = np.array(rows, dtype=float)

print("dataset loaded")

print("Shape:", data.shape)
print("Rows:", data.shape[0])
print("Columns:", data.shape[1])

print("Dimensions:", data.ndim)

print("Data Type:", data.dtype)

print(data[:5])

print(headers)

for i, column in enumerate(headers):
    missing_count = np.sum(np.isnan(data[:, i]))

    print(column, ":", missing_count)

for i, column in enumerate(headers):
    unique_values = np.unique(data[:, i])

    print(column, ":", len(unique_values))

for i, column in enumerate(headers):

    print("\nColumn:", column)
    print("Minimum:", np.nanmin(data[:, i]))
    print("Maximum:", np.nanmax(data[:, i]))
    print("Mean:", np.nanmean(data[:, i]))
    print("Median:", np.nanmedian(data[:, i]))
    print("Standard Deviation:", np.nanstd(data[:, i]))

transaction_ids = data[:, 0]


unique_ids, counts = np.unique(
    transaction_ids,
    return_counts=True
)


duplicate_ids = unique_ids[counts > 1]


print("Duplicate Transaction IDs:", duplicate_ids)
print("Number of Duplicate IDs:", len(duplicate_ids))

outlet_ids = data[:, 2]


invalid_outlets = (outlet_ids < 1) | (outlet_ids > 3)


print("Invalid outlet records:", np.sum(invalid_outlets))

quantity = data[:, 5]


invalid_quantity = quantity <= 0


print("Invalid quantity records:", np.sum(invalid_quantity))

unit_price = data[:, 6]


invalid_price = (unit_price <= 0) & (~np.isnan(unit_price))

print("Invalid unit prices:", np.sum(invalid_price))

unit_cost = data[:, 7]


invalid_cost = (unit_cost <= 0) & (~np.isnan(unit_cost))


print("Invalid unit costs:", np.sum(invalid_cost))

discount = data[:, 8]


invalid_discount = (discount < 0) | (discount > 1)


print("Invalid discount records:", np.sum(invalid_discount))

rating = data[:, 11]


invalid_rating = (
    ((rating < 1) | (rating > 5))
    & (~np.isnan(rating))
)


print("Invalid customer ratings:", np.sum(invalid_rating))

stock = data[:, 9]


negative_stock = stock < 0


zero_stock = stock == 0


print("Negative stock records:", np.sum(negative_stock))
print("Zero stock records:", np.sum(zero_stock))

product_code = data[:, 3]


category_code = data[:, 4]

product_category_mapping = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 4
}

expected_category = np.array([
    product_category_mapping[product]
    for product in product_code
])

category_mismatch = category_code != expected_category

print("Product-category mismatches:", np.sum(category_mismatch))

mismatched_records = data[category_mismatch]

print(mismatched_records)

print("Transaction IDs:", mismatched_records[:, 0])
print("Product codes:", mismatched_records[:, 3])
print("Actual categories:", mismatched_records[:, 4])
print("Expected categories:", expected_category[category_mismatch])

payment_code = data[:, 10]

invalid_payment = (payment_code < 1) | (payment_code > 4)

print("Invalid payment records:", np.sum(invalid_payment))

day_index = data[:, 1]

invalid_days = (day_index < 1) | (day_index > 30)

print("Invalid day records:", np.sum(invalid_days))

for i, column in enumerate(headers):

    missing_count = np.sum(np.isnan(data[:, i]))

    print(column, ":", missing_count)

total_missing = np.sum(np.isnan(data))

print("Total missing values:", total_missing)

clean_data = data.copy()

unit_price_index = headers.index("unit_price")

missing_price_mask = np.isnan(data[:, unit_price_index])

missing_price_records = data[missing_price_mask]

print("Records with missing unit prices:")
print(missing_price_records)

unit_cost_index = headers.index("unit_cost")

missing_cost_mask = np.isnan(data[:, unit_cost_index])

missing_cost_records = data[missing_cost_mask]

print("Records with missing unit costs:")
print(missing_cost_records)

rating_index = headers.index("customer_rating")

missing_rating_mask = np.isnan(data[:, rating_index])

missing_rating_records = data[missing_rating_mask]

print("Number of missing ratings:", len(missing_rating_records))
print(missing_rating_records)

clean_data = data.copy()

print("Original shape:", data.shape)
print("Clean data shape:", clean_data.shape)

product_code = clean_data[:, 3]
category_code = clean_data[:, 4]

expected_category = np.array([
    product_category_mapping[product]
    for product in product_code
])

category_mismatch = category_code != expected_category

print("Mismatches before correction:", np.sum(category_mismatch))

clean_data[category_mismatch, 4] = expected_category[category_mismatch]

print("Mismatches after correction:",
      np.sum(clean_data[:, 4] != expected_category))

outlet_ids = clean_data[:, 2]

invalid_outlet_mask = (outlet_ids < 1) | (outlet_ids > 3)

invalid_outlet_records = clean_data[invalid_outlet_mask]

print("Invalid outlet records:")
print(invalid_outlet_records)

print("Invalid outlet records:",
      np.sum((clean_data[:, 2] < 1) | (clean_data[:, 2] > 3)))

quantity = clean_data[:, 5]

invalid_quantity_mask = quantity <= 0

invalid_quantity_records = clean_data[invalid_quantity_mask]


print("Invalid quantity count:", np.sum(invalid_quantity_mask))

unit_price = clean_data[:, 6]

invalid_price_mask = (unit_price <= 0) & (~np.isnan(unit_price))

invalid_price_records = clean_data[invalid_price_mask]

print("Invalid unit price records:")
print(invalid_price_records)

print("Invalid unit prices:", np.sum(invalid_price_mask))

unit_cost = clean_data[:, 7]

invalid_cost_mask = (unit_cost <= 0) & (~np.isnan(unit_cost))

invalid_cost_records = clean_data[invalid_cost_mask]

print("Invalid unit cost records:")
print(invalid_cost_records)

print("Invalid unit costs:", np.sum(invalid_cost_mask))

discount = clean_data[:, 8]

invalid_discount_mask = (discount < 0) | (discount > 1)

invalid_discount_records = clean_data[invalid_discount_mask]

print("Invalid discount records:")
print(invalid_discount_records)

print("Invalid discount records:",
      np.sum(invalid_discount_mask))

rating = clean_data[:, 11]

invalid_rating_mask = (
    ((rating < 1) | (rating > 5))
    & (~np.isnan(rating))
)

invalid_rating_records = clean_data[invalid_rating_mask]

print("Invalid rating records:")
print(invalid_rating_records)

print("Invalid customer ratings:",
      np.sum(invalid_rating_mask))

unit_price = clean_data[:, 6]

high_price_mask = unit_price > 200

high_price_records = clean_data[high_price_mask]

print("Unusually high price records:")
print(high_price_records)
print("Number of records:", np.sum(high_price_mask))

valid_prices = unit_price[~np.isnan(unit_price)]

print("Highest unit price:", np.max(valid_prices))
print("Top 10 unit prices:", np.sort(valid_prices)[-10:][::-1])

product_codes = clean_data[:, 3]

for product in np.unique(product_codes):
    prices = unit_price[product_codes == product]
    prices = prices[~np.isnan(prices)]

    print(
        "Product:", int(product),
        "| Minimum:", np.min(prices),
        "| Median:", np.median(prices),
        "| Maximum:", np.max(prices)
    )

suspicious_products = [4, 7]

for product in suspicious_products:

    mask = (
        (clean_data[:, 3] == product) &
        (clean_data[:, 6] > 100)
    )

    print("\nProduct:", product)
    print(clean_data[mask][:, [0, 3, 6]])

high_price_ids = [101468, 102005, 103950]

high_price_anomaly_mask = np.isin(
    clean_data[:, 0],
    high_price_ids
)

print("High-price anomalies flagged:",
      np.sum(high_price_anomaly_mask))

discount = clean_data[:, 8]

unique_discounts, discount_counts = np.unique(
    discount,
    return_counts=True
)

for value, count in zip(unique_discounts, discount_counts):
    print("Discount:", value, "| Count:", count)

discount = clean_data[:, 8]

high_discount_mask = (discount > 0.25) & (discount <= 1)

high_discount_records = clean_data[high_discount_mask]

print("High discount records:")
print(high_discount_records)

print("Number of high discounts:",
      np.sum(high_discount_mask))

cleaning_summary = {
    "Product-category mismatches": 4,
    "Invalid outlet IDs": 2,
    "Invalid quantities": 4,
    "Invalid unit prices": 2,
    "Invalid unit costs": 2,
    "Invalid discounts": 2,
    "Invalid customer ratings": 3,
    "High unit-price anomalies": 3,
    "High discount anomalies": 5
}

for issue, count in cleaning_summary.items():
    print(issue, ":", count)

valid_transaction_mask = (
    (clean_data[:, 5] > 0) &
    (clean_data[:, 6] > 0) &
    (clean_data[:, 7] > 0) &
    (clean_data[:, 8] >= 0) &
    (clean_data[:, 8] <= 1)
)

print("Valid financial transactions:",
      np.sum(valid_transaction_mask))

print("Invalid financial transactions:",
      np.sum(~valid_transaction_mask))

missing_price_mask = np.isnan(clean_data[:, 6])
missing_cost_mask = np.isnan(clean_data[:, 7])

print("Missing unit prices:", np.sum(missing_price_mask))
print("Missing unit costs:", np.sum(missing_cost_mask))

valid_financial_mask = (
    (clean_data[:, 5] > 0) &
    (clean_data[:, 6] > 0) &
    (clean_data[:, 7] > 0) &
    (clean_data[:, 8] >= 0) &
    (clean_data[:, 8] <= 1)
)

print("Valid financial records:", np.sum(valid_financial_mask))

financial_data = clean_data[valid_financial_mask].copy()

print("Original records:", len(data))
print("Financial analysis records:", len(financial_data))
print("Financial dataset shape:", financial_data.shape)

quantity = financial_data[:, 5]
unit_price = financial_data[:, 6]

gross_sales = quantity * unit_price

print("Total Gross Sales:", np.sum(gross_sales))

discount_rate = financial_data[:, 8]

discount_amount = gross_sales * discount_rate

print("Total Discount Amount:", np.sum(discount_amount))

net_revenue = gross_sales - discount_amount

print("Total Net Revenue:", np.sum(net_revenue))

quantity = financial_data[:, 5]
unit_cost = financial_data[:, 7]

cogs = quantity * unit_cost

print("Total COGS:", np.sum(cogs))

gross_profit = net_revenue - cogs

print("Total Gross Profit:", np.sum(gross_profit))

gross_margin = (gross_profit / net_revenue) * 100

print("Overall Gross Profit Margin:", np.mean(gross_margin), "%")

overall_gross_margin = (
    np.sum(gross_profit) / np.sum(net_revenue)
) * 100

print("Overall Gross Profit Margin:", overall_gross_margin, "%")

average_transaction_value = np.mean(net_revenue)

print("Average Transaction Value:", average_transaction_value)

average_quantity = np.mean(financial_data[:, 5])

print("Average Quantity per Transaction:", average_quantity)

total_units_sold = np.sum(financial_data[:, 5])

print("Total Units Sold:", total_units_sold)

average_selling_price = np.sum(net_revenue) / total_units_sold

print("Average Selling Price per Unit:", average_selling_price)

average_cost_per_unit = np.sum(cogs) / total_units_sold

print("Average Cost per Unit:", average_cost_per_unit)

profit_per_unit = average_selling_price - average_cost_per_unit

print("Gross Profit per Unit:", profit_per_unit)

total_gross_sales = np.sum(gross_sales)
total_discount = np.sum(discount_amount)

discount_percentage = (total_discount / total_gross_sales) * 100

print("Overall Discount Percentage:", discount_percentage, "%")