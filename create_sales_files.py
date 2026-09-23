import pandas as pd
import os

# Create sample sales data
north_data = {
    "Sale ID": [1, 2, 3, 4],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Amount": [50000, 1500, 2500, 12000]
}

south_data = {
    "Sale ID": [5, 6, 7, 8],
    "Product": ["Laptop", "Headset", "Keyboard", "Monitor"],
    "Amount": [50000, 3000, 2500, 12000]
}

west_data = {
    "Sale ID": [9, 10, 11, 12, 1],
    "Product": ["Mouse", "Laptop", "Webcam", "Headset", "Laptop"],
    "Amount": [1500, 50000, 4500, 3000, 50000]
}

# Convert data into DataFrames
north_df = pd.DataFrame(north_data)
south_df = pd.DataFrame(south_data)
west_df = pd.DataFrame(west_data)

# Create the input folder if it doesn't exist
os.makedirs("mini_project/input", exist_ok=True)

# Save Excel files
north_df.to_excel("mini_project/input/sales_north.xlsx", index=False)
south_df.to_excel("mini_project/input/sales_south.xlsx", index=False)
west_df.to_excel("mini_project/input/sales_west.xlsx", index=False)

print("North sales file created.")
print("South sales file created.")
print("West sales file created.")