
# b = int 6
# a = float 2.3

# print(type('hello'))

# hEllo= 'Helo'
# print(name_input_)

'''
This is a multi line comment
'''

# print("hello", end=" Guten Tag ")
# print('David')

# input('Press Enter to begin ')

# name = input('Enter your name: ')
# age = input("Now your name is " + name + " what is your age? ")

# print(f"Your name is {name} and you are {age} years old!") 
#string concatenation also works in the print function

# x = 10
# y = 5.5
# result = x + 5 + y
# result2 = x // y # get you an integer result
# result3 = x ** y # exponential
# print(result)

# x = float(input("Enter a number: ")) 

# one = "Result is",x if x < 5 else "No result"
# print(one)
    
# q = "Bearer Goodnessme"
# z = q.split(' ')

# asc = print(ord("o"))
# compound =  False and True
# print(compound)

# De Morgan's Law.
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

# w = True
# x = True
# y = False
# z = True

# condition_1 = x and (y or z and w)
# print(condition_1)

# this will throw an error cos is in string format.
# z = int("5.5")



# number = int(input("Enter a number: "))

# if number >= 10 and number < 20:
#     new_number = float(input("Enter another number: ")) + number
#     print("The sum of these two numbers is:",new_number)
#     if new_number > 100:
#         print("That is huge!")

# x = [[0, 2, 4], 1, [6, 8, 10], 2, [[1, 2], [3, 4], [5, 6]], 3]
# # it splits into a list ['how', 'far', 'guy'] 
# # a list is made up of elements
# y = len(x)
# print(y)

# enter_string = input("Enter a string: ")
# second_string = input("Enter a string: ")
# third_string = input("Enter a string: ")
# fourth_string = input("Enter a string: ")
# fifth_string = input("Enter a string: ")

# string_list = []

# string_list.append(enter_string)
# string_list.append(second_string)
# string_list.append(third_string)
# string_list.append(fourth_string)
# string_list.append(fifth_string)


# string_indices = int(input("Enter a number: "))
# second_string_indices = int(input("Enter a number: "))
# third_string_indices = int(input("Enter a number: "))


# print("".join(string_list[string_indices]) + string_list[second_string_indices] + string_list[third_string_indices])

# if string_indices in string_list:
#     print(string_list[string_indices])
# enter_number = int(input("Enter number: "))


# s = "hello"
# word = s.replace(',', '')
# word2 = s.split(',')
# print(word)
# number = input("Enter an integer: ")

# if number.isdigit():
#     your_name = input("What is your name? ").upper()
#     print(f"Hello, {your_name}")
# else:
#     print(number.capitalize())
    

# first_word = input("Enter a word: ")
# second_word = input("Enter another word: ")

# if first_word in second_word:
#     print("The first word is contained in the second one")
# else:
#     print("The first word isn't contained in the second one")
    
# number_of_words = input("Enter a sentence: ")
# split_word = number_of_words.split(' ')
# print(f"There are {len(split_word)} words in the sentence")
# s = "hello"

# print("    *\n   ***\n  *****\n *******\n  *****\n   ***\n    *")
# n = 10
# for i in range(-1, -10+1, -2):
#     print(i)

# result = 0
# for j in range(1, 11):
#     result += j
# print(result)

# lst = [1,2, "money", True, False]

# for j in range(len(lst)):
#     print(lst[j])

# for i in lst:
#     print(i)

# for i, element in enumerate(lst):
#     print(i, element)
    

# new_list = [1,2,3,5,5,4,4]

# for i in new_list:
#     if i == 4:
#         break
#     print(i)

# for i in range(3):
#     for j in range(4):
#         print(i, j)

# old_list = [[1,2],[True, 1],[1], [13, 4], [5,6]]
# new_list = [3,4,5,7,8]

# # for a in range(len(old_list)):
# for b, element in enumerate(new_list):
#     print(b,element)


# words = ("hello", "name", "goat")
# for i in words:
#     if i == "nae":
#         print("I found the word!")
#         break
# else:
#     print("I didn't find the word")

# for idx in range(10, -1, -3):
#     print(idx, end=",")

# string1 = "aabbcsdw"
# string2 = "abbbcsdd"

# for i in range(len(string1)):
#     if string1[i] == string2[i]:
#         print(string1[i])

# lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]
# for i, j in enumerate(lst):
#     if j % 2 == 0 and i % 2 == 1:
#         print(j)




# for inner_list in new_lst:
#     result = 0
    
#     for the_list in inner_list:
#        result += the_list
    
#     print(result)


      
# num = [-2, 0, 4]

# #input are indexes of the list

# for i in range(len(num)):
#     result = num[i]
#     print(result)
    
    
    # print(i)
 

# x = [-2,0,4,5]
# for i in range(len(x)-1):
#     print(x[i] + x[i + 1])
    
# lst = [3, 3, 2, 2, 1]

# result = 0
# i = 0

# while result < 9:
    
#     result += lst[i]
#     i += 1
#     print(lst[i])
    
# i = 0
# while True:
#     number = int(input("Enter a number: "))
#     i+=1
    
#     if number == 5:
#         print(f"You entered {i} times")
#         break

# i = 0
# string_sum = 0
# while True:
#     average_len = 0
#     string = input("Enter a word: ")
    
#     if string == 'q' or string == 'quit':
#         break
    
#     string_sum += len(string)
#     i += 1
    
# print(f"The average word length is: {string_sum/i}.") 
        


# i = 0
# string_sum = 0
# while True:
#     string = input("Enter a word: ")
    
#     if string == 'q' or string == 'quit':
#         break
    
#     else:
#         string_sum += len(string)
#         i += 1
    
# if i > 0:   
#     print(f"The average word length is: {string_sum/i}.") 


# lst = [1,3,6,10,15,21]
# i = 0
# while i < len(lst):
#     print(lst[i]**2)
#     i+=1

# char = set()

# while True:
#     enter_char = input("Enter a character: ")

#     if len(enter_char) > 1:
#         break
#     if enter_char in char:
#         break
    
#     char.add(enter_char)
# print(f"Number of unique characters entered: {len(char)}")
      
#     # else:
#     #     char.add(enter_char)
#     #     print(f"Unique{len(char)}")
        
# try:
#     2 / 0
# except Exception as e:
#     print("Exception", e)
# finally:
#     print("Done")    
# raise Exception("A new error")


# numerator = input("Enter the numerator: ")
# denominator = input("Enter the denominator: ")
# try:
#     numerator = float(numerator)
# except Exception as e:
#     print("The numerator is not a number")
# try:
#     denominator = float(denominator)
# except Exception as e:
#     print("The denominator is not a number")

# try: 
#     result = numerator / denominator
#     print("The result of this division is ", result)
# except Exception as e:
#     print('This division cannot be performed.')
# except ZeroDivisionError:
#     print('You cannot divide by 0')
# finally:
    # print('Goodbye!')

# def find_all_odds(lst):
#     new_list = []
#     for i in lst:
#         if i % 2 == 1:
#             new_list.append(i)
#     return new_list


# a = find_all_odds([-1, -3, 1, 3, 2, 1])
# print(a)
# 

# def string_lengths(strings):
#     lengths = []
#     for string in strings:
#         length = len(string)
#         lengths.append(length)
#     return lengths
    
# a = string_lengths(["Hello", "this", "is", "a", "beard", "orange", "blue"])
# print(a)

# def compare_list(lst1=[], lst2=[]):
#     set_list1 = set(lst1)
#     set_list2 = set(lst2)
#     set_intersection = set_list1.intersection(set_list2)
#     print(len(set_intersection))
# compare_list(lst2=[1,2,3])

# def running_sums(numbers):
#     i = 0
#     new_list = []
#     sum_list = 0
#     while i < len(numbers):
#         sum_list += numbers[i]
#         new_list.append(sum_list)
#         i+=1
#     print(new_list)

# running_sums([5,4,2,1,5,6,4])

# def replace(lst, target, swap_value):
#     for idx in range(len(lst)):
#         element = lst[idx]

#         if element == target:
#             lst[idx] = swap_value
            


# lst = ["tim", "is", "great", "tim", "is", "tim"]
# new_lst = replace(lst, "tim", "world")
# print(new_lst)

# class Fruit():
#     def __init__(self, name, calories):
#         self.name = name
#         self.calories = calories

#         print(f"Fruit name is {self.name} and calories of about {self.calories}")

# f1 = Fruit("Apple", 13)
# # print(f1)


class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked

    def increment(self):
        if self.locked:
            raise Exception('It is locked!')
        self.count += 1
    
    def decrement(self):
        if self.locked:
            raise Exception('It is locked!')
        self.count -= 1 
    
    def print_counter(self):
        print(f"The number of count is {self.count}")

# counter1 = Counter()
# counter1.increment()
# counter1.increment()
# counter1.increment()
# counter1.decrement()
# counter1.print_counter()

# counter1.toggle_lock()
# counter1.increment()

class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError('This is invalid!')
        self._salary = salary



# p1 = Person("Tim")
# p1.salary = -15
# print(p1.salary)


class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise Exception('This is invalid time!')
        self._second = second

t = Time(60)
t.second = 59
print(t.second)