import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    consecutives = []
    current = None
    occurence = 0

    for elem in logs['num']:
        if elem in consecutives:
            current = None
            continue
        
        if current == elem:
            occurence += 1
        else:
            current = elem
            occurence = 1

        if occurence == 3:
            consecutives.append(elem)
    
    return pd.DataFrame({'ConsecutiveNums': consecutives})

# def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
#     logs['var'] = logs.num.rolling(window=3).var()
#     return pd.DataFrame(data = {'ConsecutiveNums' : logs.query('var == 0').num.unique()})

data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id':'Int64', 'num':'Int64'})

print(consecutive_numbers(logs))