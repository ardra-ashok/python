
def factorial(num):
    fact = 1
    if type(num) != int:
        return None
    elif num < 0:
        return None
    else:
        for i in range(1,num + 1):
            fact = fact*i
        return fact
    pass



print(factorial(1))
factorial("5")


print('4' * 4)


# Python code​​​​​​‌​‌‌​‌‌‌​​‌​‌​​‌‌​‌​​​​‌​ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    for ch in hexNum:
     if ((ch < '0' or ch > '9') and
         (ch < 'A' or ch > 'F')):
             return None
    decimal = int(hexNum, 16)
    return decimal
    pass


print(hexToDec('ABC'))
print(hexToDec('Not a number'))

print(int('101', 2))
print(int(8.7))
print(bool(-1) == 1)

print("----List----")
my_List = [1,2,3,4,5]
print(my_List[3:]) 
print(my_List[0:5:2]) 
print(my_List[::3])
print(my_List[::2])

for i in range(100):
 print(i)

list_1 = list(range(100))
print(list_1[::2])
print(list_1[::5])
print(list_1[::10])
print(list_1[::-1])
print(list_1[::-10])

print("---modifying list---")
my_List = [1,2,3,4]
my_List.append(5)
print(my_List)

my_List.insert(3,'a new value')
print(my_List)
my_List.remove('a new value')
print(my_List)
print(my_List.pop())
print(my_List)

while len(my_List):
 print(my_List.pop())
print(my_List)

a = [1,2,3,4,5]
b = a
a.append(6)
print(b)

a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b)
