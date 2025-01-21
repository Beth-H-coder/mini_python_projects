import random

# establish if number is an odd/even 

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