# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,

from math import sqrt


print("Введите координаты первой точки разделеннные запятой")
firstCoord  = [int(i) for i in input().split(',')[:2]]
print("Введите координаты второй точки разделеннные запятой")
secondCoord = [int(i) for i in input().split(',')[:2]]

def findDistance(firstCoord, secondCoord):
    result = sqrt((secondCoord[0] - firstCoord[0])**2 + (secondCoord[1] - firstCoord[1])**2)
    return result

print(f"{findDistance(firstCoord, secondCoord):1.2f}")