import csv
import statistics
from typing import TypedDict

file_name = "products.csv"


class Product(TypedDict):
    """
    This class is used to define the structure of the data that will be read from the CSV file.
    """

    name: str
    price: int
    quantity: int
    brand: str
    category: str
    entry_date: str  # Fechas como str (puedes convertirlas luego a datetime)


prices: list[int] = []


if __name__ == "__main__":
    with open(file=file_name, mode="r") as file:
        reader = csv.DictReader(file)
        rows: list[Product] = [
            {
                "name": row["name"],
                "price": int(row["price"]),
                "quantity": int(row["quantity"]),
                "brand": row["brand"],
                "category": row["category"],
                "entry_date": row["entry_date"],
            }
            for row in reader
        ]

        for row in rows:
            prices.append(row["price"])

    median = statistics.median(prices)
    mode = statistics.mode(prices)
    mean = statistics.mean(prices)
    stdev = statistics.stdev(prices)
    deviation = statistics.variance(prices)
    sorted_prices = sorted(prices)

    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Mean: {mean}")
    print(f"Standard deviation: {stdev}")
    print(f"Variance: {deviation}")
    print(f"Max price: {max(prices)}")
    print(f"Min price: {min(prices)}")
    print(f"Total products: {len(prices)}")
    print(f"Total price: {sum(prices)}")
    print(f"Prices sorted: {sorted_prices}")
