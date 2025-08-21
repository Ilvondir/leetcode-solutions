import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_tables = employee.merge(
        employee[['id', 'salary']],
        left_on='managerId',
        right_on='id',
        suffixes=['', '_m']
    )

    return pd.DataFrame({'Employee': merged_tables[merged_tables['salary'] > merged_tables['salary_m']]['name']})


data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
print(find_employees(employee))