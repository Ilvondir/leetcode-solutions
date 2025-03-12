import pandas as pd

def combine_two_tables1(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    person['city'] = None
    person['state'] = None

    for a in address.values:
        person.loc[person['personId'] == a[1], 'city'] = a[2]
        person.loc[person['personId'] == a[1], 'state'] = a[3]

    return person.drop('personId', axis=1)


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, how='left').drop(['personId', 'addressId'], axis=1)



person = pd.DataFrame({
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob'],
})

address = pd.DataFrame({
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California'],
})


print(combine_two_tables(person, address))