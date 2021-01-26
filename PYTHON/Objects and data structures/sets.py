fruits = { 'orange', 'apple', 'stg'}

# print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('samet')
fruits.update(['syt','grape','stg'])

fruits.remove('stg')
fruits.discard('grape')
fruits.pop()

fruits.clear()

print(fruits)

# myList = [1,3,2,4,7,1,6]
# print(myList)
# print(set(myList))