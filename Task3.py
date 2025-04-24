#a = [1, 1.1, 'a',[1], (1, 1.1), {1, 2}, {'a': 1}, None, True] # Список в котором целое; вещественное; строковое; другой список; кортеж; множество; словарь; пустой тип; булевой тип.
#a = [] # Пустой список
#b = list() # Пустой список
#a = (1, 2.1, 3) # Раньше я был кортежем
#list(a) #[1, 2.1, 3] но 'a' остался кортежем
#b = list('abc') # ['a','b','c']
#print(a)
#print([1, 1.1, 'a']) a = [1, 1.1, 'a']
#a[0]
#a[1]
#a[2]
#a[3]
#a[-1]
#a[-2]
#a[-3]
#a[-4]
#a = [1, 2, 3]
#a.index(3)
#a = [1, 1.1, 'a']
#a[0] = 'a'
#a[1] = 'б'
#a[-1] = 'в'
#a = [1, 2, 3]
#a =[1, 2, 3]
#a.append(4)
#a.append(['a','b'])
#a = [1, 2, 3]
#a.insert(0, 4)
#a = [1, 2, 3]
#a.insert(-1, 4)
#a = [1, 2, 3]
#a.extend([4, 5, 6])
#a =[1, 1.1, 'a']
#del a[0]
#del a[-1]
#del a[-1]
#del a
#a =[1, 2, 3]
#a.clear()
#a = [1, 2, 3]
#a = [1, 2, 3]
#a.pop()
#a = [1, 2, 'ab']
#a.remove('ab')
#a = [1, 2, 3]
#b = [4, 5, 6]
#c = a + b
#print(c)
#a += b
#a = [1, 2, 3]
#b = 2
#c = a *  b
#print(c)
#a *=b
#a = [1, 2, 3]
#b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#b[0]
#b[0][0]
#b(-1)[-1]
#help(list)
#a = [1, 1, 3.1]
#a.count(1)
#a = [1, 2, 3]
#a.copy()
#a = [1, 2, 3]
#a = [2, 1, 3]
#a = [2, 1, 3]
#a.sort(reverse=True)
#a = [1, 2, [1, 2, 3]]
#b = a.copy()
#b[2][0] = 10
#print(a)
#b[0] = 10
#print(a)
#from copy import deepcopy
#a = [1, 2, [1, 2, 3]]
#b = deepcopy(a)
#b[2][0] = 10
#print(a)
#a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#b = [[0] * 3] * 3
#a[0][0] = 1
#b[0][0] = 1
#a = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
#b = len(a)
#c = sum(a)
#a[4] = sum(a) // len(a)
#list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
#team1 = list_players[:total_players//2]
#team2 = list_players[total_players//2:]
#print("команда 1:", team1)
#print("команда 2", team2)
#mails = ["Письмо 1", "Письмо 2", "Письмо 3", "Письмо 4", "Письмо 5"]
#email = mails [ : : -1]
#print(email)
#emails = ["Письмо 1", "Письмо 2", "Письмо 3", "Письмо 4", "Письмо 5"]
#print("Третье письмо:", emails[2])
#print("Предпоследнее письмо:", emails[-2])
#results = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]
#count_total = len(results) #кол-во чисел
#average = sum_total / count_total
#min_score = min(results)
#max_score = max(results)
#print("среднее арифметическое всех результатов выстрелов:", average)
#print("наименьшее количество очков за выстрел:", min_score)
#print("наибольшее количество очков за выстрел:", max_score)
#fruits = ["яблоко", "банан", "опельсин", "виноград"]
#wrong_word  = fruits[2]
#correct_word = "a" + wrong_word[1 :]
#fruits[2] = correct_word
#print(fruits)
#speed = 4096
#time_minutes = 120
#cost_per_kb = 0.125
#speed_kb = speed / 1024
#time_seconds = time_minutes * 60
#file_size_kb = speed_kb * time_seconds
#paid_traffic = max(file_size_kb - 500, 0)
#traffic_cost = paid_traffic * cost_per_kb
#print(f"Размер файла в килобайтах: {file_size_kb}")
#print(f"За трафик придется заплатить: {traffic_cost}")
