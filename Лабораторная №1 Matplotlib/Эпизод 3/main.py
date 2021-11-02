import matplotlib.pyplot as plt

Preps = {}                                            # СЛОВАРЬ, ХРАНЯЩИЙ {Оценка: {Преподаватель: Сколько раз ставил}}
Groups = {}                                           # СЛОВАРЬ, ХРАНЯЩИЙ {Оценка: {НомерГруппы: Сколько раз получали}}

preps_names = ["prep" + str(i + 1) for i in range(0, 7)]                           # СПИСОК ПРЕПОДАВАТЕЛЕЙ
group_numbers = ["75" + str(i + 1) for i in range(0, 6)]                           # СПИСОК ГРУПП

for i in range(0, 10):                                                             # СОЗДАЁМ СТРУКТУРУ СЛОВАРЕЙ
    p, s = {}, {}
    for j in preps_names:
        p[j] = 0                       # НАЧАЛЬНОЕ ЗНАЧЕНИЕ - 0
    for k in group_numbers:
        s[k] = 0                       # НАЧАЛЬНОЕ ЗНАЧЕНИЕ - 0
    Preps[i + 1], Groups[i + 1] = p, s

with open("students.csv", 'r') as f:
    for line in f.readlines():
        data = line.split(';')
        Preps[int(data[2])][data[0]] += 1
        Groups[int(data[2])][data[1]] += 1

fig, ax = plt.subplots(2, 1, figsize= (10, 10))

# ПО ПРЕПОДАВАТЕЛЯМ
ax[0].bar(preps_names, Preps[3].values(), label='3')                 # НИЖЕ 3 НИКТО НЕ СТАВИЛ
p = [b for b in Preps[3].values()]                                   # СКОЛЬКО 3 ПОСТАВИЛ КАЖДЫЙ ПРЕПОДАВАТЕЛЬ
for i in range(4, 11):
    a = [b for b in Preps[i - 1].values()]
    for j in range(len(a)):
        if i != 4:
            p[j] = p[j] + a[j]
    ax[0].bar(preps_names, Preps[i].values(), bottom=p, label=i)        # ДИАГРАММА
ax[0].legend(loc = 'lower right')
ax[0].set_title('Marks per prep')

# ПО ГРУППАМ (аналогично)
ax[1].bar(group_numbers, Groups[3].values(), label='3')
s = [b for b in Groups[3].values()]
for i in range(4, 11):
    a = [b for b in Groups[i - 1].values()]
    for j in range(len(a)):
        if i != 4:
            s[j] = s[j] + a[j]
    ax[1].bar(group_numbers, Groups[i].values(), bottom=s, label=i)
ax[1].legend(loc = 'lower right')
ax[1].set_title('Marks per group')

plt.savefig("Diagram.png")
plt.show()
