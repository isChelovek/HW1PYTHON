#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# Проверка истенности ~(True|True|True) == (~(True)&~(True)&~(True))
def trueTest(firstBool, secondBool):
    return (~(firstBool[0]|firstBool[1]|firstBool[2]) == (~(secondBool[0])&~(secondBool[1])&~(secondBool[2])))

# Функция перевода десятичного целого числа в двоичное
def decToBool(x):
    binList = [False, False, False]
    count = 0
    while x > 0:
        binList[count] = (bool(x % 2))
        count = count + 1
        x = int(x / 2)
    return(binList)

#Функция печати таблицы 
def printTable(firstBool, secondBool):
    print(f"~({str(firstBool[0]):5} | {str(firstBool[1]):5} | {str(firstBool[2]):5})", end=' ')
    print(f"= ~{str(secondBool[0]):5} & ~{str(secondBool[1]):5} & ~{str(secondBool[2]):5})", end=' ')
    print(f'-> {trueTest(firstBool, secondBool)}')


for i in range(8):
    printTable(decToBool(i), decToBool(i))
