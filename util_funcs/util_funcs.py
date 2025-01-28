import random

def is_odd_or_even(num):
    if num % 2 == 0:
        return f"{num} is an even number!"
    else:
        return f"{num} is odd!"

print(is_odd_or_even(7))
print(is_odd_or_even(12))

# reverse a string - no built-in function 

def reverse_str(word):
    return word[::-1]
    
print(reverse_str("Hello world"))

# check if palindrome 

def is_palindrome(word):
    reversed = ""
    for letter in word:
        reversed = letter + reversed
    if word == reversed:
        return f"Yes, {word} is a palindrome!"
    else:
        return f"No, not a palindrome!"

print(is_palindrome('abc'))
print(is_palindrome('racecar'))

# check if a number 

def is_integer(num):
    return isinstance(num, int)

print(is_integer("5"))

# generate random num within a specified range

def randomise(num1, num2):
    return random.randrange(num1, num2)

print(randomise(1, 4))
print(randomise(8, 17))

# check if passed array contains a value 

def included_in_array(arr, item):
    if item in arr:
        return f"Yes, {item} is present at index {arr.index(item)}"

print(included_in_array(['beth', 'anna', 'fran', 'florence', 'thomas'], 'fran'))
    

# sort a list alphabetically 

def sorted(arr):
    arr.sort()
    return arr

print(sorted(['Tara', 'Anne', 'Florence', 'Thomas', 'Fran']))

# built-in sorted 
names = ['Tara', 'Anne', 'Florence', 'Thomas', 'Fran']
ordered = sorted(names)
print(ordered)

nums = [8, 7777, 255, 2, 99, 47087]
ordered_nums = sorted(nums)
print(ordered_nums)

# remove all occurrences of a value from a list 

def remove_all_items(list, item_to_exclude):
  new_list = []
  for x in list:
     if x != item_to_exclude:
        new_list.append(x)
  return new_list

print(remove_all_items(['benji', 'oscar', 'benji', 'stella', 'shivers', 'benji', 'leo'], 'benji'))

# remove first item avoiding error 

def remove_item(list, item_to_remove):
    if item_to_remove in list:
        list.remove(item_to_remove)
    return list

# using index() on lists 

def get_position(list, item):
    if item in list:
        return list.index(item)
    else:
        return "Sorry - not in the list!"

print(get_position(['apple', 'lemon', 'melon', 'banana', 'pear'], 'melon'))
print(get_position(['apple', 'lemon', 'melon', 'banana', 'pear'], 'carrot')) # ValueError if check not added 

# to loop through a list with 'range'
rhyme_dict = {}
a = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
for i in range(len(a)):
    print(i, a[i])
    rhyme_dict[i] = a[i]
print(rhyme_dict)

# built-in all 

def are_truthy(list):
    return all(list)

print(are_truthy("hello world!"))
print(are_truthy([1, 'hello', True, " "]))
print(are_truthy([0]))
print(are_truthy([False]))
print(are_truthy({'a': False}.values()))
# print(are_truthy("")) # expected False - but exception with built-in all? 


# implement own version of all() that returns True if all elements are truthy 

def all_true(data):
    for x in data:
        if not x: # checks if falsy
            return False
    return True

print(all_true(['hello', 'world', 2, True, "369"]))
print(all_true(['hello', 2, True, 0]))
print(all_true(['hello', 2, True, ""]))
print(all_true(['hello', False]))

# function to shorten time by omitting the date when passed string date of format: Friday May 2, 7pm.

def shorten_to_date(long_date):
    last_space = long_date.rfind(' ')
    return long_date[:last_space - 1]
   
print(shorten_to_date('Monday February 2, 8pm'))
print(shorten_to_date('Tuesday November 13, 10pm'))
print(shorten_to_date('Saturday August 2, 6.30am'))

mylist = ["apple", "banana", "cherry", "lemon", "pineapple"]

print(len(mylist))
print(type(mylist))
print(mylist[1])
print(mylist[-1])
print(mylist[-2])
print(mylist[:-2]) # begiinning to -2]
print(mylist[1:]) 
this_list = [1, 2, 3, 4, 5, 6, 2, 2, 2]
print(this_list[2:4])
print(this_list)
this_list.append(9)
print(this_list)
print(this_list.count(2))
this_list.reverse()
print(this_list)
num = this_list.pop(3)
print(num)
if 4 in this_list:
    print("Yes, it does exist")
# Write a Python function that takes a list of numbers and returns the sum of all the even numbers in the list.
input_list = [1, 2, 3, 4, 5, 6]

# def sum_evens(data):
#     total = 0
#     for num in data:
#         if num % 2 == 0:
#             total += num;
#     return total

# print(sum_evens(input_list))

def sum_evens(data):
    evens = [num for num in data if num % 2 == 0]
    result = sum(evens)
    return result

print(sum_evens(input_list))

input_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def filter_odd_numbers(data):
    return [num for num in data if num % 2 == 1]

print(filter_odd_numbers(input_nums))

for x in range(4, 10):
    print(x)

words_list = ['hello', 'world', 'python']

def capitalise_words(words):
    return [word.capitalize() for word in words]

print(capitalise_words(words_list))

words_list_2 = ["hello", "world", "python", "is", "awesome"]

def reverse_strings_with_condition(words):
    return [word[::-1].capitalize() if len(word) > 5 else word[::-1] for word in words]

print(reverse_strings_with_condition(words_list_2))
# Expected Output: ['olleh', 'dlrow', 'nohtyp', 'is', 'emosewa']

# def count_vowels(str):
#     count = 0
#     for char in str:
#         if char in ["a", "e", "i", "o", "u"]:
#             count += 1
#     return count

# regex 
import re

def count_vowels(str):
    res = re.findall('[aeiouAEIOU]', str)
    print('res =>', res)
    return len(res)

print(count_vowels("Hello wOrld"))

txt = "The rain in Spain falls mainly"
txt2 = "Thisisatest"
x = re.findall("ai", txt)
print(len(x))

# confirms if chars present 
y = re.search("\s", txt)
print('this is y =>', y.start()) # index of first 

if ' ' in txt:
    print('yes,exists')

txt_count = txt2.count(' ')
print(txt_count)

a = txt.endswith('y')
b = txt.endswith('x')
print(a)
print(b)

print(7 // 3 ) # 2

my_list = "beth, charlotte, thomas"
print(list(my_list))

def cookie(x):
  return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'

def sum_args(*args):
    return sum(args)

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'