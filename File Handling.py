filepath = 'file.txt'
file = open('file.txt', 'r')
# print(file.read())
#Another way to print
for char in file:
    print(char)

file.close()


#This helps you open and close the file at the same time, this is the standard and more neater way to get this done
with open('file.txt', 'r') as file:
    print(file.read())