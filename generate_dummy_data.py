import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_data(num_rows=1000, output_file="sample_data.csv"):
    data = []

    retailer_ids = [f"R{str(i).zfill(5)}" for i in range(100)]  # 100 fake retailers
    product_ids = [f"P{str(i).zfill(4)}" for i in range(20)]     # 20 fake products
    price_points = [1, 2, 5, 10, 20, 25, 30]                     # Typical scratch-off prices

    start_date = datetime(2022, 7, 1)
    end_date = datetime(2025, 6, 30)

    for _ in range(num_rows):
        retailer_id = random.choice(retailer_ids)
        retailer_name = f"Retailer_{retailer_id}"
        product_id = random.choice(product_ids)
        product_name = f"Product_{product_id}"
        price_point = random.choice(price_points)

        return_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        pack_number = random.randint(1000, 9999)
        pack_size = random.choice([20, 50, 100])
        start_ticket = random.randint(0, pack_size - 10)
        end_ticket = start_ticket + random.randint(1, 10)
        current_location = random.choice(["Returned", "Warehouse", "Transit"])

        total_price = (end_ticket - start_ticket) * price_point

        data.append([
            retailer_id,
            retailer_name,
            return_date.strftime("%m/%d/%Y"),
            product_id,
            product_name,
            pack_number,
            pack_size,
            start_ticket,
            end_ticket,
            current_location,
            price_point,
            total_price
        ])

    columns = [
        "RetailerID", "RetailerName", "ReturnDate", "ProductID", "ProductName",
        "PackNumber", "PackSize", "StartTicket", "EndTicket", "CurrentLocation",
        "PricePoint", "TotalPrice"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv(output_file, index=False)
    print(f"Generated {output_file} with {num_rows} rows.")

if __name__ == "__main__":
    generate_sample_data()
