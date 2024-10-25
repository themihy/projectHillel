# print("hello world")
from configparser import InterpolationMissingOptionError
from pydoc import resolve
from tokenize import endpats
from unittest import removeResult

from unicodedata import numeric

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
