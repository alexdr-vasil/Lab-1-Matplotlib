import pandas as pd
import matplotlib.pyplot as plt

# Ввод данных
results = pd.read_html("results_ejudge.html")[0]
students = pd.read_excel("students_info.xlsx").rename(columns={'login': 'User'})
# Слияние
merged = pd.merge(results, students, on='User')

# Графики
fig, axes = plt.subplots(1, 2, figsize=(15, 7))

title1 = "Среднее количество задач по факультетским группам"
merged.groupby('group_faculty')['Solved'].mean().plot(kind='bar', ax=axes[0], title=title1)
for tick in axes[0].get_xticklabels():
    tick.set_rotation(0)

title2 = "Среднее количество задач по группам по информатике"
merged.groupby('group_out')['Solved'].mean().plot(kind='bar', ax=axes[1], color='orange', title=title2)
for tick in axes[1].get_xticklabels():
    tick.set_rotation(0)

plt.savefig("Results.png")
plt.show()

# Кто прошёл задачи G или H
Passed = merged[(merged.G >= 10) | (merged.H >= 10)]
# Из какой группы в какую группу попал
ans = Passed[['group_faculty', 'group_out']]
print(ans)

