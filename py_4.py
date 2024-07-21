print("----Sets----")

set_1 = {'a','b','c'}
print(set_1)

set_2 = set(('a','b','c'))
print(set_2)

list_1 = ['a','b','b','c','c']
list_2 = list(set(list_1))
print(list_2)
print(type(list_2))

# Error while accessing set with any index
# print(set_1[0])

print('a' in set_1)
print('z' in set_1)

set_1.add('d')
print(set_1)

while len(set_1):
 set_1.pop()
print(set_1)
set_1 = {'a','b','c'}
set_1.discard('a')
print(set_1)


print("--------------------Tuples------------------------")
print()
tuple_1 = ('a','b','c')
print(tuple_1)
print(tuple_1[0])
# tuple_1[0] = 'd'  --- Tuples cant be modified

def test_tuple():
 return (1,2,3)
print(type(test_tuple()))

tuple_2 = 1,2,4
print(type(tuple_2))

a,b,c = test_tuple()
print(a)
print(b)
print(c)
