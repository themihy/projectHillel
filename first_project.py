# print("hello world")
# from configparser import InterpolationMissingOptionError
# from pydoc import resolve
# from selectors import SelectSelector
# from tokenize import endpats
# from turtledemo.penrose import start
# from unittest import removeResult
#
# from unicodedata import numeric

# grivna = int(input("Enter a number price: "))
# value = (input("Enter a value 1 for usd or 2 for euro: "))
#
#
# if value == "1":
#     print(grivna / 40)
# elif value == "2":
#     print(grivna / 44)
# else:
#     print("Eror")
# while True:
#     temp = int(input("Enter a temp: "))
#     if temp <= -26 or temp >= 70:
#         print("Erorr, temepature is a so big for person")
#         continue
#     elif temp == -26 or temp < 5:
#         print("Cold")
#     elif temp == 6 or temp < 25:
#         print("Normal")
#     elif temp == 26 or temp < 50:
#         print("Hot")
#     else:
#         print("Danger")
#         break
# number = int(input("Enter number:"))
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number % 100 // 10
# n4 = number % 10
# print(n1)
# print(n2)
# print(n3)
# print(n4)



#number = int(input('Enter a number:'))
#n1 = number // 10000
#n2 = number //  1000 % 10
#n3 = number % 1000 // 100
#n4 = number % 100 // 10
#n5 = number % 10
# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)
#result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
#print(result)

#number = int(input("Enter your number"))
#n1 = number // 10
#n2 = number // 100
#n3 = number // 1000

#n1 = number // 10 %
#n2 = number % 100 // 10
#n3 = number % 1000 // 100

#print(n1)
#print(n2)
#print (n3)

# number_a = 28
# number_b = 41
# result = number_a * number_b
# print (result)
#
# first_number = int(input("Enter a first number:"))
# second_number = int(input("Enter a second number"))
# result = first_number + second_number
# print(f"Hello, your lacky number is {result}")

#Калькулятор hw_1

# first_number = int(input("Enter a first number:"))
# second_number = int(input("Enter a second number:"))
# operator = input("Enter a operator")
# if operator == "+":
#     print(first_number + second_number)
# elif operator == "-":
#     print(first_number - second_number)
# elif operator == "*":
#     print(first_number * second_number)
# elif operator == "/":
#         if second_number == 0:
#             print("Error")
#             exit()
#         print(first_number / second_number)
# else:
#     print("Error")

# hw_2

# numbers = [1, 2, 3, 4, 5]
# numbers.insert(0, numbers[-1])
# numbers.pop()
# print(numbers)


#hw_3

# numbers = [1,2,3]
# number_to_add = 1
# numbers_Quantity = len(numbers)
# if numbers_Quantity % 2 == 0:
#     number_to_add = 0
#
# leftPart = numbers [: numbers_Quantity // 2 + number_to_add]
# rightPart = numbers  [ numbers_Quantity // 2 + number_to_add:]
# result = [leftPart, rightPart]
# print(result)


# i = 0
#
# while True:
#
#     if i == 2:
#         i += 1
#         print("win...")
#         continue  # пропустить подальші дії циклу, але цикл не зупиниться
#
#     if i > 5:
#         print("lose...")
#         break  # цикл зупиниться (повне завершення циклу)
#
#     print(i)
#     i += 1


# while  True:
#     rating = int(input("Enter a rating from 1 to 10:"))
#     if rating < 1 or rating > 10:
#         print("Error")
#         continue
#
#     elif rating == 0 or rating <= 3:
#         print("Bad rating")
#     elif rating == 4 or rating <= 7:
#         print("Normal rating")
#
#     elif rating == 8 or rating <= 10:
#         print("Exelent Rating")
#
#     is_continue = input("Do you want to continue? '+' or '-' ")
#     if is_continue == "-":
#         print("Exit from program")
#         break


# number = [1, 2, 4, 2, 56]
#
# for nums in number:
#     print(nums, end=" ")

# numbers = [1, 2, 4, 6, 9]
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
#
# import random
# a = random.randint (1, 10)
# print(a)
# random_list = [random.randint(1, 100) for _ in range(a)]
# print("Исходный список:", random_list)
#

#hw_4.1
#
# numbers = [1, 0, 12, 0, 7, 0, 10]
# a = 0
# for num in numbers:
#     if num != 0:
#         numbers[a]= num
#         a += 1
#
# while a < len(numbers):
#         numbers[a] = 0
#         a += 1
#
# print(numbers)

#hw4.2

# num = [1, 2, 3, 4, 5, 6 ,7, 8]
# summa_index =   sum((num[i]) for i in range (0, len(num), 2))
# print(summa_index)
#
# result = summa_index * num[-1]
# print(result)
#
# formatted_result = f"({'+'.join(str(num[i]) for i in range(0, len(num), 2))}) * {num[-1]} = {result}"
# print(formatted_result) #нашел эту формулу с интернета, если быть по честному))) Я ее до сих пор понять не могу)


#hw4.3
# import random
#
#
# length = random.randint(3, 10)
#
#
# random_list = [random.randint(1, 100) for _ in range(length)]
# print("Исходный список:", random_list)
#
#
# first_element = random_list[0]
# third_element = random_list[2]
# second_from_end = random_list[-2]
#
#
# new_list = [first_element, third_element, second_from_end]
# print("Новый список:", new_list)




########
# hw5.1
# import string
# import keyword
#
# test_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
#              'get_Value', '3m', 'm3', 'assert', 'assert_exception', 'some_super_puper__value']
#
# for test_variable in test_data:
#     if len(test_variable) > 0:
#         if test_variable in keyword.kwlist:
#             print(f"Error! Found {test_variable} is keyword!")
#         elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.count(" ") == 0:
#             is_correct = True
#             for symbol in string.punctuation.replace("_", ""):
#                 if symbol in test_variable:
#                     is_correct = False
#                     print(f"Error! Found {symbol} in variable name!")
#                     break
#
#
#             first_underscore_index = test_variable.find("_")
#             if first_underscore_index != -1:
#                 second_underscore_index = test_variable.find("_", first_underscore_index + 1)
#                 if second_underscore_index != -1 and second_underscore_index - first_underscore_index == 1:
#                     is_correct = False
#                     print(f"Error! Found double '_' in {test_variable} variable name!")
#
#             if is_correct:
#                 print(f"Keyword {test_variable} is correct!")
#         else:
#             print(f"Error! Found {test_variable} in variable name!")
#     else:
#         print("Incorrect variable length!")



#hw 5.2
# while True:
#     confirmation = "y"
#     first_number = int(input("Enter a first number:"))
#     second_number = int(input("Enter a second number:"))
#     operator = input("Enter a operator")
#     if operator == "+":
#             print(first_number + second_number)
#     elif operator == "-":
#             print(first_number - second_number)
#     elif operator == "*":
#             print(first_number * second_number)
#     elif operator == "/":
#             if second_number == 0:
#                 print("Error")
#                 exit()
#             print(first_number / second_number)
#             continue
#     else:
#         print("Error")
#         continue
#
#     is_continue = input(f"Do you want to continue? \'{confirmation}\' for yes: ")
#     if is_continue not in ['yes', 'y']:
#             print("Exit from program...")
#             break

#hw5.3
#


# user_input = input("Введіть рядок: ")
# import string
# def made_hashtag(input_string):
#     clean_string = ""
#
#     # Проход по каждому символу во входной строке
#     for i in input_string:
#
#         # Проверяем, что символ не является пунктуацией и не пробелом
#         if i not in string.punctuation and i.isalpha():
#             clean_string += i
#
#     words = clean_string.split()
#
#
#     hashtag = "#"
#     for word in words:
#         hashtag += word.title()
#
#     if len(hashtag) > 140:
#         hashtag = hashtag[:140]
#
#     return hashtag
#
#
# result = made_hashtag(user_input)
# print(result)




#hw_6.1
# import string
#
# # Вводим буквы через дефіс
# input_letters = input("Введіть дві літери через дефіс (наприклад, a-z): ")
# letter1, letter2 = input_letters.split('-')
#
# # Находим индексы букв
# start_index = string.ascii_letters.index(letter1)
# end_index = string.ascii_letters.index(letter2)
#
# # Генерируем результат
# if start_index <= end_index:
#     result = string.ascii_letters[start_index:end_index + 1]
# else:
#     result = string.ascii_letters[start_index:end_index - 1:-1] + letter2
#
# print("Символи між ними:", result)


#hw6.2
# user_input = int(input("Введіть число секунд (0-8639999): "))
# def format_time(seconds):
#     # Константы
#     seconds_in_a_minute = 60
#     seconds_in_an_hour = seconds_in_a_minute * 60
#     seconds_in_a_day = seconds_in_an_hour * 24
#
#     # Находим количество дней, часов, минут и секунд
#     days, seconds = divmod(seconds, seconds_in_a_day)
#     hours, seconds = divmod(seconds, seconds_in_an_hour)
#     minutes, seconds = divmod(seconds, seconds_in_a_minute)
#
#     # Определяем правильное слово для "день"
#     if days == 1:
#         day_word = "день"
#     elif 2 <= days <= 4:
#         day_word = "дни"
#     else:
#         day_word = "дней"
#
#     # Форматируем вывод с заполнением нулями
#     formatted_time = f"{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}"
#     return formatted_time
#
#
#
# if 0 <= user_input < 8640000:
#     result = format_time(user_input)
#     print("Час у читальному вигляді:", result)
# else:
#     print("Число повинно бути в межах від 0 до 8639999.")

#hw_6.3

# def multiply_digits(number):
#     while number > 9:
#         product = 1
#         # Перемножаем все цифры числа
#         for digit in str(number):
#             product *= int(digit)
#         number = product
#     return number
#
# # Вводим число от пользователя
# user_input = int(input("Введіть ціле число: "))
#
# # Получаем результат
# result = multiply_digits(user_input)
# print("Результат:", result)


# user_nubmer = int(input("Enter a seconds:"))
# result = user_nubmer * 2
# print(f"Квадрат числа равен: {user_nubmer} * 2=", result)


#hw7.1

# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
# # Тесты
# assert say_hi("Jojo", 42) == "Hi. My name is Jojo and I'm 42 years old", 'Test1'
# assert say_hi("Dodge", 21) == "Hi. My name is Dodge and I'm 21 years old", 'Test2'
# print('ОК')



#hw7.2
# def correct_sentence(text):
#     # Приводим первое слово к заглавной букве
#     corrected_text = text.capitalize()
#
#     # Проверяем, заканчивается ли строка точкой
#     if not corrected_text.endswith('.'):
#         corrected_text += '.'
#
#     return corrected_text
#
#
# # Тесты
# assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
# assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
#
# print('ОК')

#hw7.3
# def second_index(text, some_str):
#     first_index = text.find(some_str)
#     if first_index == -1:
#         return None  # Если первое вхождение не найдено, возвращаем None
#
#     second_index = text.find(some_str, first_index + len(some_str))
#     return second_index if second_index != -1 else None
#
# # Тесты
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
#
# print('ОК')


#hw7.4
# def common_elements():
#     # Генерация списков кратных 3 и 5
#     multiples_of_3 = {i for i in range(100) if i % 3 == 0}
#     multiples_of_5 = {i for i in range(100) if i % 5 == 0}
#
#     # Пересечение множеств
#     common = multiples_of_3.intersection(multiples_of_5)
#
#     return common
#
#
# # Тест
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('ОК')






#hw8.1

# def add_one(some_list):
#     # Перетворюємо список цифр на число
#     number = 0
#     for digit in some_list:
#         number = number * 10 + digit  # Додаємо кожну цифру
#     # Додаємо 1
#     number += 1
#     # Перетворюємо число назад у список цифр
#     return [int(digit) for digit in str(number)]
#
# # Тестування функції
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")










#hw8.2
# def is_palindrome(text):
#     # Оставляем только буквы и цифры, приводим к нижнему регистру
#     cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
#     # Проверяем, является ли очищенный текст палиндромом
#     return cleaned_text == cleaned_text[::-1]
#
# # Тестирование функции
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

#hw8.3
# def find_unique_value(some_list):
#     for num in some_list:
#         if some_list.count(num) == 1:
#             return num
#
# # Тестування функції
# assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")



#hw9.1
# def popular_words(text, words):
#     # Приводимо текст до нижнього регістру і розділяємо його на слова
#     text = text.lower().split()
#
#     # Створюємо словник для підрахунку кількості появ кожного слова
#     result = {}
#
#     for word in words:
#         # Для кожного слова з списку рахуємо його появи в тексті
#         result[word] = text.count(word)
#
#     return result
#
#
# # Тестовий приклад
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
#                      ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
#
# print('OK')


#9.2
# def difference(*args):
#     # Якщо немає аргументів, повертаємо 0
#     if not args:
#         return 0
#     # Знаходимо максимальне та мінімальне значення серед аргументів
#     max_value = max(args)
#     min_value = min(args)
#     # Обчислюємо різницю і повертаємо її
#     return round(max_value - min_value, 2)  # Округлюємо до 2 знаків після коми
#
# # Тестові приклади
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
#
# print('OK')

#hw10.1
# def some_gen(begin, end, func):
#     """
#     begin: первый элемент последовательности
#     end: количество элементов в последовательности
#     func: функция, которая формирует значения для последовательности
#     """
#     current_value = begin
#     for _ in range(end):
#         yield current_value
#         current_value = func(current_value)
#
# # Пример функции, которая возводит число в квадрат
# def pow(x):
#     return x ** 2
#
# # Тестирование генератора
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
#
# # Проверка, что это генератор
# assert isgenerator(gen) == True, 'Test1'
#
# # Проверка вывода генератора
# assert list(gen) == [2, 4, 16, 256], 'Test2'
#
# print('OK')

#h10.2
# def first_word(text):
#     """ Пошук першого слова """
#     # Видаляємо зайві пробіли на початку і в кінці
#     text = text.strip()
#
#     # Заміна розділових знаків на пробіли (також коми, крапки і т.д.)
#     for char in '.,!?;:':
#         text = text.replace(char, ' ')
#
#     # Розбиваємо рядок по пробілах і повертаємо перше слово
#     return text.split()[0]
#
#
# # Тестування:
# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')
#

#hw10.3

# def is_even(digit):
#     """ Перевірка чи є парним число """
#     return digit % 2 == 0
#
# # Тестування:
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')




#hw11.1
# def prime_generator(end):
#     # Проходимо по всіх числах від 2 до end (включно)
#     for num in range(2, end + 1):
#         # Перевіряємо, чи число просте
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):  # Перевіряємо до квадратного кореня з num
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num  # Повертаємо просте число
#
# # Тести
# from inspect import isgenerator
#
# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')
#


#hw11.2
# def generate_cube_numbers(end):
#     n = 2
#     while n**3 < end:
#         yield n**3  # Повертаємо куб числа
#         n += 1
#     return  # Завершуємо генератор, коли куб числа перевищує end
#
# # Тести
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
# print('Ok')

#hw11.3
# def is_even(number):
#     return (number & 1) == 0
#
# # Тести
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
#
# print("Ok")



#hw12.1
# import re
# import codecs
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     # Відкриваємо html-файл для читання
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html = file.read()
#
#     # Використовуємо регулярний вираз для видалення всіх HTML тегів
#     cleaned_text = re.sub(r'<[^>]*>', '', html)
#
#     # Видаляємо порожні рядки
#     cleaned_text = '\n'.join(line for line in cleaned_text.split('\n') if line.strip())
#
#     # Записуємо очищений текст у результативний файл
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(cleaned_text)
#
#
# delete_html_tags('draft.html', 'cleaned.txt')




#hw12.2
# class Item:
#     def __init__(self, name, price, description, dimensions):
#         self.name = name
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#
#     def __str__(self):
#         return f"{self.name}, price: {self.price}"
#
# class User:
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}, phone: {self.numberphone}"
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#
#     def add_item(self, item, cnt):
#         if item in self.products:
#             self.products[item] += cnt
#         else:
#             self.products[item] = cnt
#
#     def __str__(self):
#         items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
#         return f"User: {self.user}\nItems:\n{items_str}"
#
#     def get_total(self):
#         total = sum(item.price * cnt for item, cnt in self.products.items())
#         return total
#
# # Створення товарів
# lemon = Item('lemon', 5, "yellow", "small")
# apple = Item('apple', 2, "red", "middle")
#
# # Створення покупця
# buyer = User("Ivan", "Ivanov", "02628162")
#
# # Створення замовлення
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
#
# # Виведення інформації про замовлення
# print(cart)
# """
# User: Ivan Ivanov, phone: 02628162
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
#
# # Перевірка сумарної вартості
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
#
# # Додавання ще яблук
# cart.add_item(apple, 10)
#
# # Виведення інформації після оновлення
# print(cart)
# """
# User: Ivan Ivanov, phone: 02628162
# Items:
# lemon: 4 pcs.
# apple: 30 pcs.
# """
#
# # Перевірка оновленої вартості
# assert cart.get_total() == 80, 'Всього 80'



#hw13.1
# class Human:
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"
#
# class Student(Human):
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f"Student: {super().__str__()}, Record Book: {self.record_book}"
#
# class Group:
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = "\n".join(str(student) for student in self.group)
#         return f"Group Number: {self.number}\n{all_students}"
#
# # Тестування
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
#
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!


#hw13.2
# class Counter:
#     def __init__(self, current=1, min_value=0, max_value=10):
#         # Ініціалізація атрибутів поточного значення, мінімального та максимального значення
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_current(self, start):
#         """Встановлює поточне значення лічильника"""
#         if self.min_value <= start <= self.max_value:
#             self.current = start
#         else:
#             raise ValueError(f"Current value must be between {self.min_value} and {self.max_value}.")
#
#     def set_max(self, max_max):
#         """Встановлює максимальне значення лічильника"""
#         self.max_value = max_max
#         if self.current > self.max_value:
#             self.current = self.max_value
#
#     def set_min(self, min_min):
#         """Встановлює мінімальне значення лічильника"""
#         self.min_value = min_min
#         if self.current < self.min_value:
#             self.current = self.min_value
#
#     def step_up(self):
#         """Збільшує поточне значення лічильника на 1, викидаючи виняток, якщо досягнуто максимум"""
#         if self.current < self.max_value:
#             self.current += 1
#         else:
#             raise ValueError("Reached maximum value.")
#
#     def step_down(self):
#         """Зменшує поточне значення лічильника на 1, викидаючи виняток, якщо досягнуто мінімум"""
#         if self.current > self.min_value:
#             self.current -= 1
#         else:
#             raise ValueError("Reached minimum value.")
#
#     def get_current(self):
#         """Повертає поточне значення лічильника"""
#         return self.current
#
# # Тестування
# counter = Counter()
#
# # Встановлюємо поточне значення 7
# counter.set_current(7)
#
# # Збільшуємо лічильник на 3
# counter.step_up()
# counter.step_up()
# counter.step_up()
# assert counter.get_current() == 10, 'Test1'
#
# # Тепер намагаємося перевищити максимальне значення
# try:
#     counter.step_up()  # Очікується виняток
# except ValueError as e:
#     print(e)  # Достигнут максимум
# assert counter.get_current() == 10, 'Test2'
#
# # Встановлюємо мінімум на 7
# counter.set_min(7)
#
# # Тепер зменшуємо лічильник, поки не досягнемо мінімуму
# counter.step_down()
# counter.step_down()
# counter.step_down()
# assert counter.get_current() == 7, 'Test3'
#
# # Тепер намагаємося зменшити лічильник нижче мінімуму
# try:
#     counter.step_down()  # Очікується виняток
# except ValueError as e:
#     print(e)  # Достигнут минимум
# assert counter.get_current() == 7, 'Test4'

