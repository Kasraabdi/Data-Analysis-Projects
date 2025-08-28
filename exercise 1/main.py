import pandas as pd


df = pd.read_excel("messy_sales.xlsx")
print("--- Initial Data Overview ---")
df.info()
print("\n---------------------------------------\n")

print("--- Step 1: Drop Duplicate Rows ---")
df.drop_duplicates(inplace=True)
print("Duplicate rows have been dropped.")

print("\n--- Step 2: Handle Missing Values ---")
df['CustomerID'] = df['CustomerID'].fillna('Unknown')
df.dropna(subset=['Description'], inplace=True)
print("Missing values have been handled.")

print("\n--- Step 3: Correct Data Types ---")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print("'InvoiceDate' column converted to datetime.")

print("\n--- Step 4: Standardize Text Data ---")
df['Country'] = df['Country'].replace('UK', 'United Kingdom')
print("Standardized 'UK' to 'United Kingdom'.")

print("\n--- Step 5: Handle Illogical Data ---")
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
print("Rows with illogical data (negative quantity or zero price) have been removed.")

print("\n---------------------------------------")
print("\n--- Final Data Status After All Cleaning ---")
print(f"Final number of rows: {len(df)}")
df.info()