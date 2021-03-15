import numpy.random as rand

n = rand.randint(3, 10 ** 4)
min_lim = 1
max_lim = 10 ** 6
matrix = rand.randint(min_lim, max_lim, n)
# print(matrix)

m = rand.randint(1, 100)
min_li = 0
max_li = 10 ** 9
matri = rand.randint(min_li, max_li, m)
# print(matri)

k = rand.randint(1, 100)
max_limm = 100
matr = rand.randint(min_lim, max_limm, (k, m))
# print(matr)

def maxPerimeter(mas):
    maxp = 0
    n = len(mas)
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
                return "Создание треугольника невозможно"
            else:
                return "Максимальный периметр = " + str(maxp)

def maxNumber(nums):
        strums = []
        for i in nums:
            strums.append(str(i))
        result = []
        startlen = len(strums)
        while len(result) < startlen:
            max = '0'
            for i in strums:
                if len(i) < len(max):
                    if int(max) < int(i) * 10 ** (len(max) - len(i)):
                        max = i
                elif len(i) > len(max):
                    if int(i) > int(max) * 10 ** (len(i) - len(max)):
                        max = i
                else:
                    if int(i) > int(max):
                        max = i
            result.append(max)
            strums.remove(max)
        resstr = ''
        for i in result:
            resstr = resstr + i
        return resstr

def diagonalSort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(nums) - 1):
            for j in range(len(nums[0]) - 1):
                if nums[i][j] > nums[i + 1][j + 1]:
                    # Меняем элементы
                    nums[i][j], nums[i + 1][j + 1] = nums[i + 1][j + 1], nums[i][j]
                    # Устанавливаем swapped в True для следующей итерации
                    swapped = True

print("1:", maxPerimeter(matrix))
print("2:", maxNumber(matri))
diagonalSort(matr)
print("3:", matr)