print("-------------------Dictionary Comprehension-----------------")
animalList = [('a','antelope'),('b','bear'), ('c','cat'),('d','dog')]
animalDict = {item[0]:item[1] for item in animalList}
print(animalDict)

animals = {key : value for key,value in animalList}
print(animals)
print(list(animals.items()))
print([{'letter': key, 'name':value} for key,value in animals.items()])

# Example for list and Dictionary comprehension
def encode
