print("-------------------List Comprehension-----------------")

list_1 = [1,2,3,4,5]
print([2*item for item in list_1])

print("---------------List comprehension with filters-----------------")
list_2 = list(range(100))
filteredList = [item for item in list_2 if item % 10 == 0] 
print(filteredList)
filteredList = [item for item in list_2 if item % 10 < 3] 
print(filteredList)

print("---------------List comprehension with functions-----------------")

str_1 = "Hello, I am waffle maker. I makes waffles"
print(str_1.split('.'))
print(str_1.split())

def cleanWord(word):
 return word.replace('.','').lower()
list_3 = [cleanWord(word) for word in str_1.split()]
print(list_3)
list_4 = [cleanWord(word) for word in str_1.split() if len(cleanWord(word))<3]
print(list_4)

print("---------------Nested List comprehension-----------------")
list_5 = [[cleanWord(word) for word in sentence.split()] for sentence in str_1.split('.')]
print(list_5)