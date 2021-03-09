import numpy.random as rand

n = rand.randint(3,10 ** 4)
min_lim = 1
max_lim = 10 ** 6
matrix = rand.randint(min_lim,max_lim,n)
#print(matrix)

def maxPerimeter(mas):
    maxp = 0
    m = len(mas)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a = mas[i]
                b = mas[j]
                c = mas[k]
                if (a < b + c and b < a + c
                        and c < a + b):
                    maxp = max(maxp, a + b + c)
            if (maxp == 0):
                return "Невозможно создание треугольника"
            else:
                return "Максимальный периметр = " + str(maxp)

print(maxPerimeter(matrix))