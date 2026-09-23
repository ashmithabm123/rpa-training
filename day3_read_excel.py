import openpyxl

# Load the Excel file
workbook = openpyxl.load_workbook("sample_data/invoices.xlsx")

# Select the worksheet
sheet = workbook.active

total_amount = 0

# Read each invoice
for row in sheet.iter_rows(min_row=2, values_only=True):
    invoice_id = row[0]
    customer = row[1]
    amount = row[2]

    total_amount += amount

    print(f"Invoice: {invoice_id} | Customer: {customer} | Amount: {amount}")

print(f"\nTotal Invoice Amount: {total_amount}")