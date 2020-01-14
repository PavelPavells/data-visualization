import scipy as sp
from matplotlib import pyplot as plt
from collections import Counter

# TASK 1 (ВВП)

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    #Линейная диаграмма
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    #Название диаграммы
plt.title('Номинальный ВВП')

    #Подписи к осям
plt.ylabel('Млрд $')
plt.xlabel('Период')

    #Визуализация
plt.show()

# TASK 2 (ФИЛЬМЫ)

movies = ['Энни Холл', 'Бен-Гур', 'Касабланка', 'Ганди', 'Вестсайдская история']
num_oscars = [5, 11, 3, 8, 10]

# ШИРИНА ПО УМОЛЧАНИЮ 0.8 ПОЭТОМУ ПРИБАВЛЯЮ + 0.1 ЧТОБЫ ВЫРОВНИТЬ
# СТОЛБЦЫ ПО ЦЕНТРУ ИНТЕРВАЛА
xs = [i + 0.1 for i, _ in enumerate(movies)]

#[xs] - x КООРДИНАТЫ, ВЫСОТА num_oscars
plt.bar(xs, num_oscars)

plt.ylabel('Количество наград')
plt.title('Мои любимые фильмы')

# МЕТКИ С НАЗВАНИМИ ФИЛЬМОВ НА ОСИ Х
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()

# TASK 3 GISTAGRAMMA
grades = [34, 22, 12, 75, 64, 89, 90, 101, 154, 134, 135,39, 16]
decile = lambda grade: grade // 10 * 10  #DECILE = 1 / 10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x - 4 for x in histogram.keys()],  #сдвиг столбца влево на 4
                        histogram.values(), #высота столбца
                        width = 5)                  #ширина каждого столбца
plt.axis([-5, 105, 0, 5]) # x(-5, 105) y(0, 5)
plt.xticks([10 * i for i in range(11)]) #метки по оси х
plt.xlabel('Дециль')
plt.ylabel('Число студентов')
plt.title('Распределение оценок за экзамен')
plt.show()