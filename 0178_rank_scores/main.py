import pandas as pd
import numpy as np

# def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
#     rank = 1
#     scores = scores.sort_values(ascending=False, by='score').reset_index()
#     scores['rank'] = np.zeros(len(scores), dtype=int)

#     if len(scores): scores.at[0, 'rank'] = 1
#     for i in range(1, len(scores)):
#         if scores.at[i-1, 'score'] != scores.at[i, 'score']:
#             rank += 1
#         scores.at[i, 'rank'] = rank

#     return scores[['score', 'rank']]


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores['score'].sort_values(ascending=False)
    return pd.DataFrame({
        'score': scores,
        'rank': pd.Series(scores.rank(method='dense', ascending=False), dtype=int)
    })



data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
print(order_scores(scores))