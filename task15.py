'''Иван Васильевич пришел на рынок и решил купить два арбуза: 
один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей,
а для тещи полегче. 
Но вот незадача: арбузов слишком много и он не знает как же выбрать 
самый легкий и самый тяжелый арбуз? 
Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9'''

# Решение 1.
''' n = int(input("Введите количество всех арбузов: "))
weights = list(map(int, input("Введите вес арбуза: ").split()))
max_weight = min_weight = weights[0]
for weight in weights:
    if weight > max_weight:  # если текущий вес больше максимального
        max_weight = weight  # обновляем максимальный вес
    if weight < min_weight:  # если текущий вес меньше минимального
        min_weight = weight  # обновляем минимальный вес
print(min_weight, max_weight) '''


# Решение 2.
count_wm = int(input("Введите количество всех арбузов: "))
min_wm = int(input("Введите вес арбуза: "))
max_wm = min_wm
min_wm_i = max_wm_i = 0
for i in range(1, count_wm):
    wm = int(input("Введите вес арбуза: "))
    if wm > max_wm:
        max_wm = wm
        max_wm_i = i
    if wm < min_wm:
        min_wm = wm
        min_wm_i = i
print(f"самый тяжелый арбуз, весом {max_wm} кг., лежит {max_wm_i+1}-м, а самый лёгкий, весом {min_wm} кг., лежит {min_wm_i+1}-м")
