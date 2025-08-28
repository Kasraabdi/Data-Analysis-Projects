import pandas as pd
import numpy as np

# داده های اولیه
data = {
    'InvoiceNo': ['536365', '536365', '536366', '536367', '536367', '536368', '536368', '536369', '536370', '536370'],
    'StockCode': ['85123A', '71053', '84406B', '84879', '22745', '22960', 'POST', '37370', '22728', '21730'],
    'Description': ['White HANGING HEART T-LIGHT HOLDER', 'WHITE METAL LANTERN', 'CREAM CUPID HEARTS COAT HANGER', 'ASSORTED COLOUR BIRD ORNAMENT', 'POPPY\'S PLAYHOUSE BEDROOM', 'JAM MAKING SET WITH JARS', np.nan, 'ROUND SNACK BOXES SET OF 4 FRUITS', 'ALARM CLOCK BAKELIKE PINK', 'GLASS STAR FROSTED T-LIGHT HOLDER'],
    'Quantity': [6, 6, 8, 32, 6, 6, 3, 6, 24, -6], # دارای مقدار منفی
    'InvoiceDate': ['12/1/2010 8:26', '12/1/2010 8:26', '12/1/2010 8:28', '12/1/2010 8:34', '12/1/2010 8:34', '12/1/2010 8:34', '12/1/2010 8:35', '12/1/2010 8:35', '12/1/2010 8:45', '12/1/2010 8:45'],
    'UnitPrice': [2.55, 3.39, 2.75, 1.69, 2.1, 4.25, 18.0, 0, 3.75, 4.25], # دارای مقدار صفر
    'CustomerID': [17850, 17850, 17850, 13047, 13047, '13047', np.nan, 13047, 12583, 12583], # دارای نوع داده متفاوت و جای خالی
    'Country': ['United Kingdom', 'United Kingdom', 'UK', 'United Kingdom', 'France', 'France', 'France', 'United Kingdom', 'UK', 'France'] # دارای مقادیر متناقض
}

messy_df = pd.DataFrame(data)

# اضافه کردن ردیف تکراری
duplicate_row = pd.DataFrame([data], columns=data.keys())
messy_df = pd.concat([messy_df, messy_df.iloc[[0]]], ignore_index=True)

# ذخیره در فایل اکسل
messy_df.to_excel("messy_sales.xlsx", index=False)

print("The messy_sales.xlsx file was successfully created!")