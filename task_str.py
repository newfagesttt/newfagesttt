# ЗАДАЧА 1

volume_dicket = 1.44 * 1024 * 1024
page = 100
line = 50
symbol = 25
inf_symbol = 4
volume_book = page * line * symbol * inf_symbol
num_book = volume_dicket // volume_book
print(num_book)

# ЗАДАЧА 2
storona = 5
radius = 5
pi = 3.1415
s_krug = pi * radius ** 2
dlina_okr = 2 * pi * radius
P_kvadrat = 4 * storona
S_kvadrat = storona ** 2

# ЗАДАЧА 3
str_numbers  = 20 * '0' + 50 * '1' + 30 * '2'
print(str_numbers)

#ЗАДАЧА 4
speed = 4096
time = 120
coast = 500
tarif = speed *  time * coast
print(tarif)