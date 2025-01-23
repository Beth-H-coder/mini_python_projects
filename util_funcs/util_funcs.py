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
print('- - all_true function - -')
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