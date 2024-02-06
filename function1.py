#1 about grams
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2 temperature
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit_temperature = float(input("Enter the temperature in Fahrenheit: "))

celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

print(f"The equivalent temperature in Celsius is: {celsius_temperature:.2f} degrees Celsius")

#3 classic puzzle
def solve(numheads, numlegs):
    y = (numlegs - 2*numheads) / 2
    x = numheads - y
    
    if y >= 0 and x >= 0 and y == int(y) and x == int(x):
        return int(x), int(y) 
    else:
        return "No solution"  

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)
print("Number of chickens and rabbits are:", result)

#4 prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
# Example usage
numbers_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = filter_prime(numbers_list)
print("Prime numbers from the list:", prime_numbers)

#5 string
from itertools import permutations

def print_permutations(input_string):
    perms = permutations(input_string)
    
    for perm in perms:
        print(''.join(perm))

# Example usage
input_string = input("Enter a string: ")
print("Permutations of the string:")
print_permutations(input_string)

#6 revers words
def reverse_sentence(input_string):
    words = input_string.split()

    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence
# Example usage:
input_string = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(input_string)
print("Reversed sentence:", reversed_sentence)

#7 True
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))       # Output: True
print(has_33([1, 3, 1, 3]))     # Output: False
print(has_33([3, 1, 3]))        # Output: False

#8 return true
def spy_game(nums):
    position = 0
    
    for num in nums:
        if num == [0, 0, 7][position]:
            position += 1
        if position == 3:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))  # Output: True
print(spy_game([1,0,2,4,0,5,7]))  # Output: True
print(spy_game([1,7,2,0,4,5,0]))  # Output: False

#9 volume
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print("The volume of the sphere is:", volume)

#10 set,list,unique elements
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

# Example usage:
input_list = [1, 2, 3, 3, 4, 5, 5, 6, 6]
result_list = unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", result_list)

#11 palindrome
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
# Example usage:
input_word = input("Enter a word or phrase: ")
if is_palindrome(input_word):
    print(f"'{input_word}' is a palindrome!")
else:
    print(f"'{input_word}' is not a palindrome.")

#12 histogram
def histogram(int_list):
    for num in int_list:
        print('*' * num)
  
# Example usage:
histogram([4, 9, 7])

#13 guess the number
import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break
guess_the_number()
      
#14
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

def histogram(int_list):
    for num in int_list:
        print('*' * num)

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break
        









