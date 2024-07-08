# #Python Iterators and Generators

# list_instance = [1, 2, 3,4]
# iterator = iter(list_instance)
# print(next(iterator))

# #Generators
# def factors(n):
#     factor_list = []
#     for val in range(1, n+1):
#         if n % val == 0:
#             yield val

# factors_of_20 = factors(20)
# print(factors_of_20)

# #Lambda Function and Mapping

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# def square(num_list: list):
#     return[i**2 for i in num_list]

# print(square(num))

# #List comprehension to get the square of the odd numbers

# squares = [x**2 for x in num if x > 0 and x < 20 if x % 2 == 1]

# # print(squares)

# # #List comprehension to get the square of the prime numbers

# # prime = [n for n in num if all (n % i != 0 for i in range (2, n)) and n > 1]
# # prime_square = [n**2 for n in num if all (n % i != 0 for i in range (2, n)) and n > 1]
# # print(prime)
# # print(prime_square)

# # words = ["add", "subtract", "multiply", "divide"]

# # capital = [word.capitalize() for word in words]

# # print(capital)

# # strings = [word for word in words if len(word) > 4]
# # print(strings)

# #Create a list of tuples where each tuple contain the number and its cube
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# List = [(n, n**3) for n in num]
# print(List)

both = ["Fizzbuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range (1, 100)]
print(both)