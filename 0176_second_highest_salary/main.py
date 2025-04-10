import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'SecondHighestSalary': [employee['salary'].drop_duplicates().sort_values(ascending=False).iloc[1] if employee['salary'].drop_duplicates().shape[0] > 1 else None]
    })


data = [[1, 100], [2, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

print(second_highest_salary(employee))