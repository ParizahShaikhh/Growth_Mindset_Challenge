import pandas as pd

# Sample Data
data = {
    "ID": [1, 2, 3, 4, 5, 6],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Age": [25, 30, 28, 35, 25, 40],
    "Salary": [50000, 60000, None, 75000, 50000, None],  # Some missing values
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Joining Date": ["2022-01-15", "2021-06-20", "2020-03-12", "2019-08-05", "2022-01-15", "2018-12-10"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as Excel
df.to_excel("test_data.xlsx", index=False)
print("Excel file saved as test_data.xlsx")
