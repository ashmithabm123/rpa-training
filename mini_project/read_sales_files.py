import pandas as pd
import os
import sys

from openpyxl import load_workbook
from openpyxl.styles import Font


# Add parent folder to Python path
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from logger_utils import Logger


# Create logger
logger = Logger()


# Input and output paths
input_folder = "mini_project/input"
output_file = "mini_project/output/master_sales.xlsx"


# Excel files to read
files = [
    "sales_north.xlsx",
    "sales_south.xlsx",
    "sales_west.xlsx"
]


def read_excel_files(input_folder, files):
    """Read all regional Excel files."""

    dataframes = []

    for file in files:
        file_path = os.path.join(input_folder, file)

        df = pd.read_excel(file_path)
        dataframes.append(df)

        logger.info(f"Read file: {file}")

    return dataframes


def remove_duplicates(df):
    """Find and remove duplicate records."""

    duplicates = df[df.duplicated()]

    print("\nDuplicate records:")
    print(duplicates)

    print("\nNumber of duplicates:", len(duplicates))

    logger.info(f"Found {len(duplicates)} duplicate record(s).")

    cleaned_df = df.drop_duplicates()

    logger.info(
        f"Removed duplicates. Final records: {len(cleaned_df)}"
    )

    return cleaned_df


def calculate_summary(df):
    """Calculate sales summary."""

    total_sales = df["Amount"].sum()
    average_sales = round(df["Amount"].mean(), 2)
    highest_sale = df["Amount"].max()

    logger.info("Sales summary calculated.")

    return total_sales, average_sales, highest_sale


def create_master_file(
    df,
    output_file,
    total_sales,
    average_sales,
    highest_sale
):
    """Create master Excel file with summary sheet."""

    # Create output folder if it doesn't exist
    output_folder = os.path.dirname(output_file)

    if output_folder:
        os.makedirs(output_folder, exist_ok=True)

    # Save main sales data
    df.to_excel(output_file, index=False)

    logger.info("Master Excel file created.")

    # Open workbook
    workbook = load_workbook(output_file)

    # Create Summary sheet
    summary_sheet = workbook.create_sheet("Summary")

    summary_sheet["A1"] = "Sales Summary"

    summary_sheet["A2"] = "Total Sales"
    summary_sheet["B2"] = total_sales

    summary_sheet["A3"] = "Average Sale"
    summary_sheet["B3"] = average_sales

    summary_sheet["A4"] = "Highest Sale"
    summary_sheet["B4"] = highest_sale

    summary_sheet["A5"] = "Total Records"
    summary_sheet["B5"] = len(df)

    # Format heading
    summary_sheet["A1"].font = Font(
        bold=True,
        size=14
    )

    # Format column headings
    for cell in summary_sheet[1]:
        cell.font = Font(bold=True)

    # Set column widths
    summary_sheet.column_dimensions["A"].width = 20
    summary_sheet.column_dimensions["B"].width = 18

    # Save workbook
    workbook.save(output_file)

    logger.info("Summary sheet created and formatted.")


try:
    logger.info("Excel consolidation process started.")

    # Read all Excel files
    dataframes = read_excel_files(
        input_folder,
        files
    )

    # Combine all DataFrames
    combined_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    print("\nCombined Sales Data:")
    print(combined_df)

    print("\nTotal records:", len(combined_df))

    logger.info(
        f"Combined {len(files)} Excel files."
    )

    # Remove duplicates
    cleaned_df = remove_duplicates(
        combined_df
    )

    print("\nData after removing duplicates:")
    print(cleaned_df)

    print(
        "\nRecords after removing duplicates:",
        len(cleaned_df)
    )

    # Calculate sales summary
    total_sales, average_sales, highest_sale = calculate_summary(
        cleaned_df
    )

    print("\nSales Summary:")
    print("Total Sales:", total_sales)
    print("Average Sale:", average_sales)
    print("Highest Sale:", highest_sale)

    # Create master Excel file
    create_master_file(
        cleaned_df,
        output_file,
        total_sales,
        average_sales,
        highest_sale
    )

    print("\nMaster Excel file created successfully!")
    print("Saved to:", output_file)

    print("\nSummary sheet formatted successfully!")

    logger.info(
        "Excel consolidation process completed."
    )


except Exception as e:
    logger.error(
        f"Excel consolidation failed: {e}"
    )

    print("\nError:", e)


