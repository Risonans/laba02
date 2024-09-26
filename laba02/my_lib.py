import numpy as np

# Функция поиска n чисел Фибоначчи
# Принимает n
# Возвращает список из чисел
# Пример: 4 -> 0, 1, 1, 2
# Классы эквивалентности цифры, буквы, специальные символы
# Граничные значения по int
def fibonnaci(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    if n >= 3:
        mas = np.array([])
        for i in range(n):
            if i == 0: mas = np.append(mas, fibonnaci(i))
            if i == 1 or i == 2: mas = np.append(mas, fibonnaci(i))
            if i>=3:
                mas = np.append(mas, fibonnaci(i-1) + fibonnaci(i-2))
        return mas

# Функция сортировки пузырьком по возрастанию и убыванию
# Принимает mas, x
# Возвращает список из чисел
# Пример: [3, 2, 1, 7], 1 -> [1, 2, 3, 7]; [3, 2, 1, 7], 2 -> [7, 3, 2, 1]
# Классы эквивалентности: массивы, буквы, цифры, специальные символы
# Граничные значения по int
def bubble(mas, x):
    if mas == []: return 0
    if x == 1:
        for i in range(len(mas) - 1):
            for j in range(len(mas) - 1 - i):
                if mas[j] > mas[j + 1]:
                    mas[j], mas[j + 1] = mas[j + 1], mas[j]
        return mas
    if x == 2:
        for i in range(len(mas) - 1):
            for j in range(len(mas) - 1 - i):
                if mas[j] < mas[j + 1]:
                    mas[j], mas[j + 1] = mas[j + 1], mas[j]
        return mas

# Функция калькулятора (+, -, *, /)
# Принимает a, b, sim
# Возвращает число
# Пример: 1, 2, + -> 3
# Классы эквивалентности: цифры, буквы, специальные символы
# Граничные значения по int
def calculator(a,b, sim):
    if isinstance(a, int) and isinstance(b, int) and isinstance(sim, str):
        if sim == '+':
            return a+b
        elif sim == '-':
            return a-b
        elif sim == '*':
            return a*b
        elif sim == '/':
            return a/b
        else: return "Неверно заданы параметры"
    else: return "Неверно заданы параметры"