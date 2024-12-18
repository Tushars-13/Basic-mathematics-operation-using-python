import math
import cmath
from math import gcd
from functools import reduce
# reduce applies the gcd function cumulatively to the items of the list, starting with the first two elements and continuing until the entire list is reduced to a single value.

def leapYear(y):
    print()
    print("Checking if the year is a leap year or not.........")
    print()
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("The year is a leap year.")
    else: 
        print("The year is not a leap year.")
    print()
    print("----------------------------------")
    print()
 
def simp_Calc(a, b, o):
   
    if o == "+":
        res = a + b
    elif o == "-":
        res = a - b
    elif o == "*":
        res = a * b
    elif o == "/":
        res = a / b
    else:
        print("Invalid operator entered for this calculator.")
        return  # Exit if the operator is invalid to avoid printing an undefined `res`
    print("Result is:", res)
    print()
    print("----------------------------------")
    print()

def Armstrong(n):
    sum = 0
    temp = n
    num = str(n)
    count = len(num)

    while n!=0:
        digit = n%10
        sum += digit ** count
        n = n/10
    if sum == temp:
        print("The given no. is Armstrong.")
    else:
        print("The given no. is not Armstrong.")
    print()
    print("----------------------------------")
    print()

def palindrome(num):
    reverse = 0
    temp = num
    while temp != 0:
        digit = temp%10
        reverse = reverse*10 + digit
        temp = temp//10
    if reverse == num:
        print("The given no. is a Palindrome.")
    else:
        print("The given no. is not a Palindrome.")
    print()
    print("----------------------------------")
    print() 
    
def factorial(num):
    if num<0:
        print("The factorial can't be calculated for negative numbers.")
    if num == 1 or num == 1:
        return 1
    return num*factorial(num-1)

def fib(n):
    if n== 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
def is_prime(num):
    if num <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of the number
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    s = 0 # starting sum = 0
    while num!=0:
        s+= num%10
        num//=10
    return s

def find_gcd(numbers):
    result = reduce(gcd, numbers)
    return result

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def find_lcm(numbers):
    return reduce(lcm, numbers)

def is_perfect_number(number):
    if number <= 0:
        return False  # Perfect numbers are positive integers
    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i
    return divisors_sum == number

def solve_quadratic():
    print("Solving the quadratic equation ax^2 + bx + c = 0")
    
    # Taking input from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    # Calculating the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculating the two solutions using the quadratic formula
    solution1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    solution2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    # Displaying the solutions
    print(f"The solutions are: {solution1} and {solution2}")

def temp_conversion():
    print("1. Celsius to Fahrenheit and Kelvin.")
    print("2. Fahrenheit to Celsius and Kelvin.")
    print("3. Kelvin to Celsius and Fahrenheit")
    print()

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {fahrenheit}°F and {kelvin} K.")
    
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"{fahrenheit}°F is equal to {celsius}°C and {kelvin} K.")
    
    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f"{kelvin}K is equal to {celsius}°C and {fahrenheit}°F.")
    
    else:
        print("Invalid choice! Please choose a valid option.")

def base_conversion():
    print("1. Binary to Decimal, Octal, Hexadecimal")
    print("2. Decimal to Binary, Octal, Hexadecimal")
    print("3. Octal to Decimal, Binary, Hexadecimal")
    print("4. Hexadecimal to Decimal, Binary, Octal")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        binary_num = input("Enter the binary number: ")
        number = int(binary_num, 2)
        print(f"Decimal: {number}, Octal: {oct(number)[2:]}, Hexadecimal: {hex(number)[2:].upper()}")
    
    elif choice == 2:
        decimal_num = int(input("Enter the decimal number: "))
        print(f"Binary: {bin(decimal_num)[2:]}, Octal: {oct(decimal_num)[2:]}, Hexadecimal: {hex(decimal_num)[2:].upper()}")
    
    elif choice == 3:
        octal_num = input("Enter the octal number: ")
        number = int(octal_num, 8)
        print(f"Decimal: {number}, Binary: {bin(number)[2:]}, Hexadecimal: {hex(number)[2:].upper()}")
    
    elif choice == 4:
        hex_num = input("Enter the hexadecimal number: ")
        number = int(hex_num, 16)
        print(f"Decimal: {number}, Binary: {bin(number)[2:]}, Octal: {oct(number)[2:]}")
    
    else:
        print("Invalid choice! Please choose a valid option.")


def switch_statement(choice):
    match choice:
        case 1:
            year = int(input("Enter the year: "))
            leapYear(year)
        case 2:
            a = int(input("Enter operand 1: "))
            o = input("Enter the operator (+, -, /, *): ")
            b = int(input("Enter operand 2: "))
            simp_Calc(a, b, o)
        case 3:
            print("Definition:- An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits.")
            print()
            num = int(input("NOW, Enter the no.: "))
            Armstrong(num)
        case 4:
            print("Definition:- A palindrome number is a number that reads the same backward as forward.")
            print()
            num = int(input("NOW, Enter the no.: "))
            palindrome(num)
        case 5:
            num = int(input("Enter the no. to find the factorial of it: "))
            print("The Factorial of the given no. is :",factorial(num))
            print()
            print("----------------------------------")
        case 6: 
            n = int(input("Enter the no. of tems: "))
            print(f"The fibonacci series upto {n} terms is :", end= " ")
            for i in range(n):
                print(fib(i), end=" ")
            print()
            print("----------------------------------")
        case 7:
            print("A prime no. is a number which don't have any factors other than 1 and the number itself.")
            n = int(input("Enter your number: "))
            print("Checking if prime or not.")
            print()
            if is_prime:
                print("Yes, The given no. is a prime number.")
            else:
                print("No, The given no. is not a Prime number.")
            print()
            print("----------------------------------")
        case 8:
            print("Finding the Gcd of the numbers.")
            print("Enter your numbers with a space between them and when completed press ENTER.")
            numbers = list(map(int, input().split()))
            result = find_gcd(numbers)
            print(f"The GCD of your entered number is: {result}.")
            print()
            print("----------------------------------")
        case 9:
            print("Finding lcm.")
            print("Enter your numbers with a space between them and when completed press ENTER.")
            numbers = list(map(int, input().split()))
            result = find_lcm(numbers)
            print(f"The LCM of the numbers you entered is: {result}.")
            print()
            print("----------------------------------")            
        
        case 10:
            print("Choose a conversion option:")
            base_conversion()
            print()
            print("----------------------------------")

        
        case 11:
            num = int(input("Enter the number: "))
            print("Printing the sum of the digits of the given number....")
            res = sum_of_digits(num)
            print(f"The sum of the digits of {num} is: {res}.")
            print()
            print("----------------------------------")
        case 12:
            print("Definition:- A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding the number itself.")
            num = int(input("Enter a number to check if it's a perfect number: "))
            if is_perfect_number(num):
                print(f"{num} is a perfect number.")
            else:
                print(f"{num} is not a perfect number.")
            print()
            print("----------------------------------")
        case 13:
            print("Calculating the power of a number...")
            num = int(input("Enter the number: "))
            power = int(input("Enter the power of that number: "))
            answer = num ** power
            print(answer)
            print()
            print("----------------------------------")
        case 14:
            print("converting temperature....")
            temp_conversion()
            print()
            print("----------------------------------")
        case 15:
            print("Solving Quadratic Equation.....")
            solve_quadratic()
            print()
            print("----------------------------------")
            
        case _:
            print("Invalid choice, Enter your choice again.")
print()
print("-------------------------------------------------")
print()
print("1. Check if the year is a leap year or not.")
print("2. Simple Calculator.")
print("3. Check whether the number is Armstrong or not.")
print("4. Check whether the number is palindrome or not.")
print("5. Find the factorial of a number.")
print("6. Find the Fibonacci series up to n terms.")
print("7. Check if the number is prime or not.")
print("8. Find the Greatest Common Divisor (GCD) of numbers.")
print("9. Find the Least Common Multiple (LCM) of two numbers.")
print("10. Convert a number between Binary, Octal, Decimal, and Hexadecimal.")
print("11. Find the sum of digits of a number.")
print("12. Check if a number is perfect.")
print("13. Calculate the power of a number.")
print("14. Convert temperature between Celsius, Fahrenheit, and Kelvin.")
print("15. Solve a quadratic equation.")
print("99. EXIT")

while True:
    print()
    choice = int(input("Enter your choice: "))
    print()
    if choice == 99:
        print("Exiting Program.")
        break
    else:
        switch_statement(choice)
        
    




    

    
