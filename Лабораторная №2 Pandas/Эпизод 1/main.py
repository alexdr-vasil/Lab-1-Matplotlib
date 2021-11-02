import pandas as pd

df = pd.read_csv('transactions.csv', index_col='Unnamed: 0')
print('\n Задача 1:\n  Три самых крупных перевода со статусом "ОК"')
ans1 = (df.loc[df['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False))
print(ans1.iloc[0:3], "\n")

print('Задача 2:\n Полная сумма реальных платежей Umbrella, Inc:', end= ' ')
ans2 = ans1.loc[ans1['CONTRACTOR'] == 'Umbrella, Inc'].loc[:, 'SUM']
ans2 = list(ans2)
print(sum(ans2))


