'''
Небольшая записка:
Почти все реализованно в виде функций, к некоторомы написаны пояснения. 
Все ответы выводятся в консоль. 
В первом задании, для получения резульата, необходимо ввести n в консоли.
В данном модуле очень много принтов, что может усложнить чтение кода - 
они сделаны для более красивого вида при выводе ответов в консоль.
К некоторым функциям были написаны простые тесты для самопроверки.
Для того, чтобы проверить правильноть работы, передавайте свои данные в аргументы функций
'''



#1) Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов
print('Task 1.')

n = int(input('Enter N: '))
summ = 0
for i in range(1, n + 1): #с N включенным 
    if i % 2 == 0:
        summ += i
print(f'First method using for, {summ=}')

summ = 0
i = 1
while i <= n: #с N включенным 
    if i % 2 == 0:
        summ += i
    i += 1
print(f'First method using while, {summ=}')
#для того, чтобы не проверять каждый раз значение на четность, можно сразу двигаться с шагом 2 от четного значения
summ = sum([i for i in range(2, n + 1, 2)])
print(f'Third method using for with step = 2, {summ=}')
print('---'*50)



#2) Найти самое длинное слово из массива. Реализовать двумя видами циклов
print('Task 2.')

lst = [
    "глубокий", "доступный", "защитить", "методический", "непрерывный", "ответственный", "проектировать", "уникальный", 
    "функциональный", "характерный", "целеустремленный", "эффективный", "юмор", "яркий", "целеустремленный2", "целеустремленный3", 
    "целеустремленный4",
]

def max_len_word(lst: list) -> None: 
    '''
    Функция находит последнее самое длинное слово, 
    если будет несколько слов одинаковой длинны -  
    предыдущие не будут учитываться. 
    '''
    mx_ln_word = ''
    mx_len = 0
    for word in lst:
        if mx_len <= len(word):
            mx_ln_word = word
            mx_len = len(word)
    print(f'Using for: {mx_ln_word}')
    
    mx_ln_word = ''
    mx_len = 0
    i = 0
    while i <= len(lst):
        if mx_len <= len(word):
            mx_ln_word = word
            mx_len = len(word)
        i += 1
    print(f'Using while: {mx_ln_word}')

max_len_word(lst)

print('---'*50)



#3) Расчет факториала числа с выводом каждого шага.
print('Task 3.')

def fact(n: int) -> None:
    f = 1
    print('Steps:')
    print(f'{1}. {0} = {1}')
    for i in range(1, n + 1):
        f *= i
        print(f'{i+1}. {i} = {f}')    

    print(f'Factorial {n} = {f}')   
        
fact(8)

print('---'*50)



#4) Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()
print('Task 4.')

def each_third(lst: list) -> None:
    for ind, val in enumerate(lst):
        if ind % 3 == 0:
            print(f'{ind}. {val}')

lst = [1, 2, 3, 4, 'Tom', 'Mike', 5, 77, 43, 'Toddler', 'Rrrr', 'Dada', 123, 321, 234, 234, 111, 'Topi4', 1444]
each_third(lst)

print('---'*50)



#5) Напечатать таблицу умножения для числа n, использовать f строки
print('Task 5.')

def table(n: int) -> None:
    print(f'==== X {n} ====')
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')

table(12)

print('---'*50)



#6) Подсчитать количество цифр в числе. Реализовать двумя видами циклов
print('Task 6.')

def num_count(n: int) -> None:
    print(f'Number: {n}')
    tmp_n = n
    counter = 0
    while tmp_n > 0:
        counter += 1
        tmp_n //= 10
    print(f'Using while: {counter}')
    
    tmp_n = n
    counter = 0
    for _ in str(tmp_n):
        counter += 1
    print(f'Using for: {counter}')   
    
    print(f'Flex method: {len(str(n))}')
    
num_count(12322)

print('---'*50)



#7) Проверить, является ли строка палиндромом (зеркальная)
print('Task 7.')

def is_polindrome(string: str) -> bool:
    '''
    В этой функции я вначале привожу строку к нормальному виду (удаляя все пробелы, приводя ее к нижнему регистру и т.п)
    т.к не знаю, какие тесты будут.
    '''
    string = string.replace(' ', '').lower()
    string = ''.join([i for i in string if i.isalpha()])
        
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True

print(f'А роза упала на лапу Азора - {is_polindrome('А роза упала на лапу Азора')}')

#Tests 
assert is_polindrome('А роза упала на лапу Азора') == True
assert is_polindrome('Уж редко рукою окурок держу') == True
assert is_polindrome('Аргентина манит негра') == True
assert is_polindrome('Диван незаразен на вид') == True
assert is_polindrome('А в Енисее - синева') == True
assert is_polindrome('О, духи, от уборки микробу-то и худо') == True

print('---'*50)



#8) Определить, содержит ли список дубликаты
print('Task 8.')

def has_double(lst: list) -> bool:
    #True - сореджит дубликаты, False - нет. 
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

lst = [1, 2, 3, 4, 5, 5]
print('Standard method: ')
print(f'{lst} - {has_double(lst)}')
#Tests:
assert has_double([1, 2, 3, 4, 5, 6, 7]) == False
assert has_double([1, 2, 3, 4, 5, 6, 7, 7]) == True
assert has_double([1, 2, 3, 4, 5, 6, 7, 'Tom', 'Mom', 'Dom']) == False 
assert has_double([44, 55, 66, 77, 99]) == False
assert has_double([44, 55, 66, 77, 99, 44, 52]) == True

#PS. flex method 
print('Flex method: ')
print(len(lst) != len(set(lst)))

print('---'*50)



#9) Удалить все дубликаты из списка без использования дополнительных структур. 
# Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
print('Task 9.')

def delete_doubles(lst: list) -> list:
    i = 0
    length = len(lst)
    while i < length:
        j = i + 1
        while j < length:
            if lst[i] == lst[j]:
                lst.pop(j)
                length -= 1
                j -= 1
            j += 1
        i += 1
    return lst
lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'Tom', 'Mark', 'Dad', 2, 'Tom']
print(f'{lst}\n{delete_doubles(lst)}')

#Tests:
assert delete_doubles([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert delete_doubles([1, 2, 3, 4, 5, 6, 7, 3]) == [1, 2, 3, 4, 5, 6, 7]
assert delete_doubles([5, 4, 3, 1, 1, 1, 4, 3, 5]) == [5, 4, 3, 1]
assert delete_doubles([4, 3, 2, 1, 1, 2, 3, 4, 'Dad', 'Tom', 'Dad']) == [4, 3, 2, 1, 'Dad', 'Tom']
assert delete_doubles(['Tim', 'Tom', 'Tim', 4.23, 4.23, 'Dad', 'Tim']) == ['Tim', 'Tom', 4.23, 'Dad']

print('---'*50)



#10) Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]
print('Task 10.')

def reverse_str(string: str) -> str:
    new_str = ''
    for i in range(len(string) - 1, -1, -1):
        new_str += string[i]
    return new_str

print(f'Hellow words - {reverse_str('Hellow words')}')
print(f'MIN MAX MAX MAX - {reverse_str('MIN MAX MAX MAX')}')
print('---'*50)



#11) Напечатать календарь месяца, предполагая, что месяц начинается в понедельник и имеет 31 день
print('Task 11.')

print('Пн Вт Ср Чт Пт Сб Вc')
i = 1
while i <= 31:
    if len(str(i)) == 1:
        print(f' {i}', end=' ')
    else:
        print(i, end=' ')
    if i % 7 == 0:
        print() 
    i += 1