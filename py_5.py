
from collections import defaultdict
print("---------------------Dictionaries-------------------------")

animals ={
 'a':'aardwolf',
 'b': 'bear',
 'c': 'cat'
}
print(animals)
print(animals['a'])
animals['d'] = 'dog'
animals['a'] = 'antelope'
print(animals)
print(animals.keys())
print(animals.values())
print(animals.get('a'))
print(animals.get('e'))
print(animals.get('e','elephant'))
print(len(animals))

animals = {
 'a': ['aardwolf','antelope' ],
 'b': ['bear'],
}
animals['b'].append('bison')
print(animals)

if 'c' not in animals:
 animals['c'] = []
animals['c'].append('cat')
print(animals)

print("---------------Default dictionaries------------------")
animals = defaultdict(list)
print(animals)
animals['e'].append('elephant')
print(animals)
animals['e'].append('emu')
print(animals)
print(animals['f'])
