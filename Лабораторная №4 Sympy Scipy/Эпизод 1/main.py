from sympy import symbols, Eq, solve, Matrix

# Создаём символы ро, мю, лямбда и икс
rho, mu, lmbd, x = symbols('rho mu lambda x')

# Создаём матрицу A системы
A = Matrix([[Matrix.zeros(3), -Matrix.eye(3) / rho, Matrix.zeros(3)],
            [-Matrix.eye(3) * mu, Matrix.zeros(3, 6)],
            [Matrix.zeros(3, 9)]])
B = Matrix([[0, 0, 0, -lmbd - mu, 0, 0, -lmbd, 0, -lmbd], [Matrix.zeros(8, 9)]]).T
A += B

# Для нахождения собственных значений и детерминанта создадим матрицу
# (A - Lambda * E),   Lambda - собственное значение, E - единичная матрица
A_lambda = A - Matrix.eye(9) * x

# Найдём определитель этой матрицы, и приравняв его к 0 решим уравнение
det = A_lambda.det()
eq = Eq(det, 0)
Lambdas = solve(eq, x)

# Вывод
for i, val in enumerate(Lambdas):
    print("Lambda " + str(i + 1) + " =", val)
