import numpy as np
import matplotlib.pyplot as plt

# Создаем два случайных массива
x = np.random.rand(50)  # Создаем массив x из 100 случайных чисел от 0 до 1
y = np.random.rand(50)  # Создаем массив y из 100 случайных чисел от 0 до 1
 

# Расчет корреляции Пирсона
def pearson_correlation(x, y):
    n = len(x)  # Количество элементов в массиве
    sum_x = np.sum(x)  # Сумма всех элементов массива x
    sum_y = np.sum(y)  # Сумма всех элементов массива y
    sum_x_sq = np.sum(x ** 2)  # Сумма квадратов элементов массива x
    sum_y_sq = np.sum(y ** 2)  # Сумма квадратов элементов массива y
    sum_xy = np.sum(x * y)  # Сумма произведений соответствующих элементов массивов x и y

    numerator = n * sum_xy - sum_x * sum_y  # Числитель формулы корреляции Пирсона
    denominator = np.sqrt((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2))  # Знаменатель формулы корреляции Пирсона

    correlation = numerator / denominator  # Вычисление корреляции Пирсона
    return correlation


# Выводим результат и строим график
print("Корреляция Пирсона:", pearson_correlation(x, y))  # Выводим значение корреляции Пирсона
plt.scatter(x, y)  # Строим график рассеяния для массивов x и y
plt.show()  # Отображаем график