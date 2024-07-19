
# list
list_1 = [1,2,3,4]
print(list_1)

list_2 = ["test1","test2","test4"]
print(list_2)

list_3 = ["test1",1,"test4",4]
print(list_3)
print(len(list_1))

# set
set_1 = {1,2,3,4}
print(set_1)
set_2 = {1,1,2,2}
print(len(set_2))
print([1,2]==[2,1])
print({1,2,3}=={3,2,1})

# tuples
tuple_1 = (1,2,3)
print(len(tuple_1))
print((1,2)==(2,1))
list_1.append(2)
print(list_1)
# error - tuples cant be modified once created
# print(tuple_1.append(2))

# Dictionaries
dictionary_1 = {
 'apple': 'A fruit',
 'bear': 'An animal',
 'apple': 'A tasty fruit',
}
print(dictionary_1["apple"])
