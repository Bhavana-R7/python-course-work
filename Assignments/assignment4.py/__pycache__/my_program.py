#my_programs.py
# my_programs.py

def armstrong_number():
    print("Program: Armstrong Number")
    print(""" 
def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return num == total
    """)
    print("Test Case 1: is_armstrong(153) -> True")
    print("Test Case 2: is_armstrong(123) -> False")
    print("Explanation: An Armstrong number equals the sum of its digits "
          "raised to the power of number of digits.")

def swap_numbers():
    print("Program: Swap Two Numbers")
    print("""
def swap(a, b):
    a, b = b, a
    return a, b
    """)
    print("Test Case 1: swap(10, 20) -> (20, 10)")
    print("Test Case 2: swap(5, -1) -> (-1, 5)")
    print("Explanation: Uses tuple unpacking to swap two values.")

def count_vowels():
    print("Program: Count Vowels in String")
    print("""
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)
    """)
    print("Test Case 1: count_vowels('hello') -> 2")
    print("Test Case 2: count_vowels('sky') -> 0")
    print("Explanation: Loops through characters and counts vowels.")

def gcd_two_numbers():
    print("Program: GCD of Two Numbers")
    print("""
import math
def gcd(a, b):
    return math.gcd(a, b)
    """)
    print("Test Case 1: gcd(12, 18) -> 6")
    print("Test Case 2: gcd(5, 7) -> 1")
    print("Explanation: Uses Euclidean algorithm via math.gcd().")

def reverse_number():
    print("Program: Reverse a Number")
    print("""
def reverse_number(n):
    return int(str(n)[::-1])
    """)
    print("Test Case 1: reverse_number(1234) -> 4321")
    print("Test Case 2: reverse_number(100) -> 1")
    print("Explanation: Converts number to string and reverses it.")

def sum_of_digits():
    print("Program: Sum of Digits")
    print("""
def sum_digits(n):
    return sum(int(d) for d in str(n))
    """)
    print("Test Case 1: sum_digits(123) -> 6")
    print("Test Case 2: sum_digits(987) -> 24")
    print("Explanation: Iterates digits and sums them.")

def count_words():
    print("Program: Count Words in a Sentence")
    print("""
def count_words(sentence):
    return len(sentence.split())
    """)
    print("Test Case 1: count_words('Hello world') -> 2")
    print("Test Case 2: count_words('Python is fun') -> 3")
    print("Explanation: Splits string by spaces and counts words.")

def string_title_case():
    print("Program: Convert String to Title Case")
    print("""
def title_case(s):
    return s.title()
    """)
    print("Test Case 1: title_case('hello world') -> 'Hello World'")
    print("Test Case 2: title_case('python function') -> 'Python Function'")
    print("Explanation: Uses built-in title() method.")

def fibonacci_series():
    print("Program: Fibonacci Series")
    print("""
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
    """)
    print("Test Case 1: fibonacci(5) -> [0, 1, 1, 2, 3]")
    print("Test Case 2: fibonacci(7) -> [0, 1, 1, 2, 3, 5, 8]")
    print("Explanation: Each number is sum of previous two.")

def prime_check():
    print("Program: Prime Number Check")
    print("""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    """)
    print("Test Case 1: is_prime(7) -> True")
    print("Test Case 2: is_prime(10) -> False")
    print("Explanation: Checks divisibility up to sqrt(n).")

def factorial_number():
    print("Program: Factorial of a Number")
    print("""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    """)
    print("Test Case 1: factorial(5) -> 120")
    print("Test Case 2: factorial(0) -> 1")
    print("Explanation: Uses recursion to calculate factorial.")

def palindrome_string():
    print("Program: Palindrome String Check")
    print("""
def is_palindrome(s):
    return s == s[::-1]
    """)
    print("Test Case 1: is_palindrome('madam') -> True")
    print("Test Case 2: is_palindrome('python') -> False")
    print("Explanation: Compares string with its reverse.")

def decimal_to_binary():
    print("Program: Decimal to Binary Conversion")
    print("""
def decimal_to_binary(n):
    return bin(n).replace("0b", "")
    """)
    print("Test Case 1: decimal_to_binary(10) -> '1010'")
    print("Test Case 2: decimal_to_binary(7) -> '111'")
    print("Explanation: Uses Python’s bin() function.")

def largest_of_three():
    print("Program: Largest of Three Numbers")
    print("""
def largest(a, b, c):
    return max(a, b, c)
    """)
    print("Test Case 1: largest(3, 9, 5) -> 9")
    print("Test Case 2: largest(10, 10, 5) -> 10")
    print("Explanation: Uses built-in max() function.")

def custom_sort():
    print("Program: Custom Sort Ascending Order")
    print("""
def custom_sort(lst):
    return sorted(lst)
    """)
    print("Test Case 1: custom_sort([3,1,2]) -> [1,2,3]")
    print("Test Case 2: custom_sort([9,5,7]) -> [5,7,9]")
    print("Explanation: Uses built-in sorted() function.")