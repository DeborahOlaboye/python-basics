#Python Iterators and Generators

list_instance = [1, 2, 3,4]
iterator = iter(list_instance)
print(next(iterator))

#Generators
def factors(n):
    factor_list = []
    for val in range(1, n+1):
        if n % val == 0:
            yield val

factors_of_20 = factors(20)
print(factors_of_20)

#Lambda Function and Mapping

num = [1, 2, 3, 4]
def square(num_list: list):
    return[i**2 for i in num_list]

print(square(num))