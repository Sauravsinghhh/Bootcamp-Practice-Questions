import math

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

print("Original list:", numbers)

# Adding a number to the list
numbers.append(23)
print("After adding 23:", numbers)

# Removing a number from the list
numbers.remove(5)
print("After removing 5:", numbers)

# Finding the sum of all numbers in the list
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)

# Finding the average of the numbers
average = total_sum / len(numbers)
print("Average of the numbers:", average)

# Finding the maximum and minimum numbers in the list
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

# Squaring each number in the list using list comprehension
squared_numbers = [x ** 2 for x in numbers]
print("Squared numbers:", squared_numbers)

# Finding the square root of each number in the list using map and math.sqrt
sqrt_numbers = list(map(math.sqrt, numbers))
print("Square roots of the numbers:", sqrt_numbers)

# Filtering the list to get only even numbers using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Calculating the product of all numbers in the list using a loop
product = 1
for number in numbers:
    product *= number
print("Product of all numbers:", product)

# Calculating the factorial of the first number in the list
factorial_first = math.factorial(numbers[0])
print("Factorial of the first number:", factorial_first)
