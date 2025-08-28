# 📊 Sales Data Analysis & Cleaning Project

This project demonstrates a complete workflow for cleaning and analyzing a messy, real-world sales dataset.

> The primary goal is to take raw, imperfect data and transform it into a clean, usable format for analysis, simulating a common task for a data analyst.

---

## ✨ Key Features

-   **Dirty Data Generation:** The `create_messy_data.py` script generates an Excel file (`messy_sales.xlsx`) containing common data issues like missing values, duplicates, and incorrect data types.
-   **Data Cleaning:** The `main.py` script reads the raw data, identifies all issues, and applies cleaning techniques to fix them.
-   **Feature Engineering:** After cleaning, a new feature (`TotalPrice`) is calculated and added to the dataset to enable further analysis.

---

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### Prerequisites

Make sure you have Python installed. You will also need the following libraries:
- `pandas`
- `numpy`

You can install them using pip:
```bash
pip install pandas numpy