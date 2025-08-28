# 🚢 Titanic Survival Analysis

This project is an exploratory data analysis (EDA) of the classic Titanic dataset. The goal is to clean the data, find statistical correlations, and visualize the key factors that influenced passenger survival.

## Analysis Workflow

1.  **Data Loading & Exploration**: The dataset is loaded from a `titanic.csv` file and inspected for initial issues like missing values and incorrect data types.
2.  **Data Cleaning & Preprocessing**:
    * Missing values in `Age`, `Cabin`, and `Embarked` are handled.
    * Categorical features (`Sex`, `Embarked`) are converted to numerical values.
    * A new binary feature `HasCabin` is engineered from the `Cabin` column.
    * Unnecessary columns are dropped.
3.  **Correlation Analysis**: A correlation matrix and a `seaborn` heatmap are generated to find statistical relationships between all numerical variables.
4.  **Visualization & Insights**: Various plots (`barplot`, `histplot`) are created to visualize key relationships and confirm findings, such as the impact of gender and passenger class on survival.

## How to Run

1.  **Prerequisites**: Ensure you have a `titanic.csv` file in the same directory as the notebook.
2.  **Install Libraries**:
    ```bash
    pip install pandas seaborn matplotlib numpy
    ```
3.  **Execute Notebook**: Open and run the cells sequentially in the `titanic_analysis.ipynb` Jupyter Notebook.