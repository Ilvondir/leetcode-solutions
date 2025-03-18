import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    return pd.DataFrame({
        f'getNthHighestSalary({N})': [employee['salary'].drop_duplicates().sort_values(ascending=False).iloc[N-1] if employee['salary'].drop_duplicates().shape[0] > N-1 and N > 0 else None]
    })

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id':'Int64', 'salary':'Int64'})

print(employee['salary'].drop_duplicates().sort_values(ascending=False))

print(nth_highest_salary(employee, 0))