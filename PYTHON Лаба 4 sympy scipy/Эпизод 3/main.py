import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy import symbols, Function, Eq, dsolve, solve, sqrt, lambdify


# Функция, задающая уравнение для Scipy
def model(y, x):
    dydx = -2 * y
    return dydx


# Символы
y = symbols('y', cls=Function)
x, c1 = symbols('x C1')

# Решение через Sympy
diff_equation = Eq(y(x).diff(), -2 * y(x))                        # дифференциальное уравнение
solution = (dsolve(diff_equation, y(x)))                          # общее решение
c = solve(solution, c1)[0].evalf(subs={x: 0, y(x): sqrt(2)})      # начальные условия, находим константу
y_ans = solve(solution, y(x))[0].evalf(subs={c1: c})              # частное решение - ответ
print('Решение Sympy:  y(x) =', y_ans)                            # вывод

# Создание списка для графика Sympy
x_values = np.arange(0, 10.1, 0.1)
f = lambdify(x, y_ans, 'numpy')
sympy_ans = f(x_values)

# Решение Scipy
scipy_ans = odeint(model, 2**0.5, x_values)[:, 0]


# Графики решений Sympy и Scipy
plt.plot(x_values, sympy_ans)
plt.plot(x_values, scipy_ans, '--')
# Сетка
plt.grid(which='major', color='k', linewidth=1)
plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()
# Подписи осей, легенда
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend(["Решение SymPy", "Решение SciPy"])
# Сохранение и вывод
plt.savefig('sympy_scipy_solutions.png')
plt.show()


# Разница между Sympy и Scipy
difference = abs(scipy_ans - sympy_ans)


# График разницы
plt.plot(x_values, difference)
# Сетка
plt.grid(which='major', color='k', linewidth=1)
plt.grid(which='minor', color='grey', linestyle=':')
plt.minorticks_on()
# Подписи осей, легенда
plt.xlabel('x')
plt.ylabel('dy(x)')
plt.legend(["Разница решений SymPy и SciPy"])
# Сохранение и вывод
plt.savefig('difference.png')
plt.show()
