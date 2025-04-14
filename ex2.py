import math


num = float(input("Введите число больше 2: "))


while num >= 2:
    num = math.sqrt(num)
    print(f"{num:.3f}")
