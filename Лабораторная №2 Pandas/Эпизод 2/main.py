import pandas as pd
import matplotlib.pyplot as plt

# Вывод данных
df = pd.read_csv('flights.csv')
PriceWeight = df.groupby('CARGO').sum()[['PRICE', 'WEIGHT']]
Numbers = df.groupby('CARGO').count()['Unnamed: 0']
print("\nПолная стоимость и вес:")
print(PriceWeight)
print("\nКоличество рейсов:")
print(Numbers)

# подписи для легенды (подписи снаружи выглядят некрасиво)
l = ["Jumbo", 'Medium', 'Nimble']
# функция подписей внутри областей
my_autopct = lambda p: '{:.0f}'.format((p / 100) * PriceWeight['PRICE'].sum())

# График полной стоимости
PriceWeight['PRICE'].plot(kind='pie', labels=None, autopct=my_autopct)
plt.title("Полная стоимость рейсов компании")
plt.legend(loc='best', labels=l)
plt.savefig('Prices')
plt.show()

# График полного веса
PriceWeight['WEIGHT'].plot(kind='pie', labels=None, autopct=my_autopct)
plt.title("Полный вес, перевезённый компанией")
plt.legend(loc='best', labels=l)
plt.savefig('Weights')
plt.show()

# График количества рейсов
Numbers.plot(kind='pie', labels=None, autopct=my_autopct)
plt.title("Полное количество рейсов компании")
plt.legend(loc='best', labels=l)
plt.savefig('Numbers')
plt.show()
