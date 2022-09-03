# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def findArea(x, y):
    if (x > 0) & (y > 0):
        return 1
    elif (x < 0) & (y > 0):
        return 2
    elif (x < 0) & (y < 0):
        return 3
    elif (x > 0) & (y < 0):
        return 4 
    else:
        return -1


x = int(input('Введите значение координаты Х = '))
y = int(input('Введите значение координаты Y = '))

area = findArea(x, y)
print(area)
if (area > 0):
    print(f"Координаты x = {x} и y = {y} принадлежат оси {area}")
else:
    print("Некоректный ввод значений X и Y")