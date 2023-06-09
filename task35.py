''' Напишите функцию, которая принимает одно число 
и проверяет, является ли оно простым
Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes '''
def is_prime(n, div=2):       
    if n < 2:                        # Если число меньше 2, оно не является простым
        return False    
    if n == 2:                       # Если число равно 2, оно простое
        return True    
    if div > n**0.5:                # Если делитель стал больше, чем корень из n, значит,
        return True                 # уже были проверены все возможные делители, и n простое    
    if n % div == 0:                # Если n делится без остатка на div, то оно не простое
        return False    
    return is_prime(n, div+1)       # Рекурсивно проверяем следующий делитель

''' def is_prime2(n):               # Эта функция на работает (123, 125 показывает не верно)
    for i in range(2,n):
        if n%i == 0:
            return False
        else:
            return True '''
        

number = int(input("Введите число: "))
print(is_prime(number))
''' print(is_prime2(number)) '''