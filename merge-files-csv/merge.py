import pandas as pd

listDados = [
    'ca-2019-02.csv',
    'ca-2020-01.csv',
    'ca-2020-02.csv',
    'ca-2021-01.csv',
    'ca-2022-01.csv',
    ]

# listDados = [
#     'merging-2016_2019.csv',
#     'merging-2019_2021.csv'
# ]

df_total = []
for item in listDados:
    df = pd.read_csv(f'files/{item}',on_bad_lines='skip')
    df_total.append(df)


data = pd.concat(df_total)
#data = pd.concat(df_total, axis=1, join='inner')

data.to_csv('files/merging-2016_2021.csv')
