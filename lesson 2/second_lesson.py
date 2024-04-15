#1) Попросите пользователя ввести строку и выведите ее в обратном порядке, не используя метод reverse() и sorted().
def reverse_without_methods(txt: str) -> str:
    return txt[::-1]
print('Task 1:')
text = input('txt: ')
print(reverse_without_methods(text))
print('-' * 50)


#2) Замените в пользовательской строке все появления буквы h на букву H, кроме первого и последнего вхождения.
def replace_h(txt: str) -> str:
    if txt.count('h') <= 2:
        return txt
    first = txt.index('h') + 1
    second = txt.rfind('h')
    new_txt = txt[:first] + txt[first:second].replace('h', 'H') + txt[second:]
    return new_txt


#3) Выведите количество слов в строке
def words_count(txt: str) -> int:
    return len(txt.split())


#4) Выведите количество слов в строке, не используя метод split()
def words_count_without_split(txt: str) -> int:
    if not txt:
        return 0
    txt = txt.strip()
    return txt.count(' ') + 1


#5) У Вас есть строка, состоящая из двух слов, разделенных пробелом. 
# Переставьте эти слова местами.Результат запишите в строку и выведите получившуюся строку.
def words_swap(txt: str) -> str:
    new_txt = ' '.join(txt.split()[::-1])
    return new_txt
 
    
#6) Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека.
# Вам необходимо вывести фамилию и инициалы.
def format_initials(txt: str) -> str:
    txt = txt.split()
    new_txt = f'{txt[0]} {txt[1][0].upper()}. {txt[2][0].upper()}.'
    return new_txt

    
#7) Создайте список-матрешку, в который поместите два элемента: целое число и вложенный список, 
# в который поместите еще два элемента: вещественное число и вложенный список, в который поместите 
# еще два элемента: комплексное число и вложенный список, в который поместите еще три элемента: 
# пустой список целое число и строку "Иголка". Выведите на экран конечную строку.
lst = [1, [1.1, [2 + 3j, [[], 1, 'Иголка']]]]
print('Task 7:')
print(lst[1][1][1][2])
print('-' * 50)


#8) Объедините два списка в один список двумя способами.
lst_1 = list(range(5))
lst_2 = list(range(5, 11))
print('Task 8:')
print(lst_1 + lst_2)
lst_1.extend(lst_2)
print(lst_1)
print('-' * 50)


#9) Соедините два списка и отсортируйте их. Затем удалите повторяющиеся элементы.
def combine_two_lsts(lst_1: list, lst_2: list) -> list:
    return sorted(set(lst_1 + lst_2))
   
    
#10) Проверить, все ли числа в произвольной последовательности уникальны.
def if_unique(lst: list) -> bool:
    return len(lst) == len(set(lst))


#11) Дан словарь: date_dict = {'year': 2024, 'month': 4, 'day': 14} ->'2024-4-14'
date_dict = {'year': 2024, 'month': 4, 'day': 14}
date_1 = '-'.join(list(map(str, date_dict.values())))
#date_2 = '-'.join([str(i) for i in date_dict.values()])
print('Task 11:')
print(date_1)
print('-' * 50)

#12) На вход от пользователя поступает строка с числами, разделёнными запятой. Вам нужно составить список и кортеж с этими числами.
def make_lst_and_tuple() -> None:
    print('Task 12(строка с числами, разделёнными запятой):')
    string_with_nums = input()
    lst = string_with_nums.split(', ')
    tup = tuple(lst)
    print(f'List: {lst}\nTuple:{tup}')
    print('-' * 50)

make_lst_and_tuple()

#13) Вам дано множество студентов...:
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print('Task 13:')
print(f'Study and work: {students & employees}')
print(f'Work and not study: {employees - students}')
print(f'Work or study but not both: {students.symmetric_difference(employees)}')
print('-' * 50)

#14) Вам дан произвольный двумерный список... транспортнирование - это когда строки столбцы становятся строками
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]

def matrix_transp(array: list) -> list:
    new_arr = []
    arr_len = len(array)
    col_len = len(array[0])
    for i in range(col_len):
        tmp_arr = []
        for j in range(arr_len):
            tmp_arr.append(array[j][i])
        new_arr.append(tmp_arr)
    return new_arr
print('Task 14:')
print(matrix_transp(array))
print('-' * 50)
    
#15) Выведите на экран следующую пирамидку....
print('Task 15:')
for i in range(5):
    print(f'X{'x' * (i * 2)}X')
print('-' * 50)



#TESTS:
#1
assert reverse_without_methods('Hellow') == 'wolleH'
assert reverse_without_methods('good morning') == 'gninrom doog'
assert reverse_without_methods('hello world') == 'dlrow olleh'
assert reverse_without_methods('how are you') == 'uoy era woh'
assert reverse_without_methods('thank you') == 'uoy knaht'
assert reverse_without_methods('have a nice day') == 'yad ecin a evah'

#2
#В этом задании я не считал H за первое или последнее вхождение, считал только h.
assert replace_h('hellow heh looweh') == 'hellow HeH looweh'
assert replace_h('The horse is happy.') == 'The Horse is happy.'
assert replace_h('She has a hat.') == 'She Has a hat.'
assert replace_h('He is in the house') == 'He is in the house'
assert replace_h('They have high hopes') == 'They Have HigH hopes'
assert replace_h('The hill is steep') == 'The hill is steep'

#3
assert words_count("The quick brown fox jumps over the lazy dog") == 9
assert words_count("Hello, world!") == 2
assert words_count("This is a test sentence.") == 5
assert words_count("") == 0
assert words_count("One") == 1

#4
assert words_count_without_split("The quick brown fox jumps over the lazy dog") == 9
assert words_count_without_split("Hello, world!") == 2
assert words_count_without_split("This is a test sentence.") == 5
assert words_count_without_split("") == 0
assert words_count_without_split("One") == 1
assert words_count_without_split("   Hello world!  ") == 2
assert words_count_without_split("One Two Three Four Five") == 5
assert words_count_without_split("123 456 789 0") == 4

#5
assert words_swap("Hello world") == "world Hello"
assert words_swap("quick lazy") == "lazy quick"
assert words_swap("a test") == "test a"
assert words_swap("Python great") == "great Python"
assert words_swap("Three Four") == "Four Three"

#6
assert format_initials("Смирнов Александр Иванович") == "Смирнов А. И."
assert format_initials("Абрамова Екатерина Петровна") == "Абрамова Е. П."
assert format_initials("Васильева Мария Сергеевна") == "Васильева М. С."
assert format_initials("Петров Петр Петрович") == "Петров П. П."
assert format_initials("Сидоров Иван Семенович") == "Сидоров И. С."

#9
assert combine_two_lsts([1, 2, 3], [2, 3, 4]) == [1, 2, 3, 4]
assert combine_two_lsts([5, 6, 7], [4, 5, 6]) == [4, 5, 6, 7]
assert combine_two_lsts([], [1, 2, 3]) == [1, 2, 3]
assert combine_two_lsts([1, 2, 3], []) == [1, 2, 3]
assert combine_two_lsts([], []) == []

#10
assert if_unique([1, 2, 3, 4, 5]) == True
assert if_unique([1, 2, 3, 4, 4]) == False
assert if_unique([]) == True
assert if_unique([1, 2, 3, 3, 3]) == False
assert if_unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True

#7, 8, 11, 12, 13, 15 в консоли 