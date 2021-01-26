# def changeName(n):
#     n = 'ada'

# name = 'yiğit'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara','izmir']

# change(sehirler[:])

# print(sehirler)

def add(*params): # tuple kullanırken * tek yıldız kullanılır
    print(type(params))
    sum = 0
    for n in params:
        sum = sum +n 
    return sum
        

print(add(10,20,50))
print(add(10,20,30))
print(add(10,20,30,40,50,60,150,200))

def displayUser(**args): # dictionary kullanırken ** çift yıldız kullanılır
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name='Samet', age = 17, city = 'istanbul')
displayUser(name='Hasan', age = 16, city = 'istanbul', phone = '05324851154')
displayUser(name='Yiğit', age = 13, city = 'kocaeli', phone = '05356457896', email = 'hacı@gmail.com')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')