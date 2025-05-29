# Пример использования
for i in range (3) :
    print (i+1, "шаг цикла")
print ("Первый цикл закончился!")

a = {1: 'x', 2: 'y', 3: 'z'}
for index, value in a.items():
    print(f'"Позиция": {index} -> "Значение": {value}')
#Перебор значений коллекции с помощью for
list for value in [1, 2, 3, 4, 5]: print(value)
tuple for value in (1, 2, 3, 4, 5): print(value)
set for value in {1, 2, 3, 4, 5}: print(value)

range(start, stop, step)
range (10)
range (1, 11)
range(1, 11, 2)
range (10, 0, -1)

for tuple_ in enumerate (["a", "б", "в"]): print(tuple_)
["a", "б", "в"]
(0, 'a')
(1, 'б')
(2, 'в')

for pos, value in enumerate("aбв", start=1)
    print("Позиция:", pos, "->", "Значение:", value)

    numbers = [10, 20, 30, 40, 50]
    total = 0
    for i in range(len(numbers)
        total += numbers[i]
        print("Суммф чисел:", total)

# a, s, p = 1, 150, 200
# while True:
        if a>10:
    break
    a += 2
    P += a
    s += p