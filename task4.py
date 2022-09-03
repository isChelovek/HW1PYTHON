def findCoord(area):
    if  (area == 1):
        return "x > 0 и y > 0"
    elif (area == 2):
        return "x < 0 и y > 0"
    elif (area == 3):
        return "x < 0 и y < 0"
    elif (area == 4):
        return "x > 0 и y < 0"
    else:
        return -1


area = int(input('Введите номер четверти '))


result = findCoord(area)

if (type(result) == type("")):
    print(f"Координаты должны быть {result}")
else:
    print("Некоректный ввод")
