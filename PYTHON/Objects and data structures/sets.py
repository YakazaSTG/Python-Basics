fruits = { 'orange', 'apple', 'ahmet'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('bla')
fruits.update(['syt','grape','ahme'])

fruits.remove('ahmet')
fruits.discard('grape')
fruits.pop()

fruits.clear()

print(fruits)

# myList = [1,3,2,4,7,1,6]
# print(myList)
# print(set(myList))
