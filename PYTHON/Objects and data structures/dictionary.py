# key -value

# 41 => kocaeli 34 => istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('istanbul')])

# print(plakalar['kocaeli'])  => 41
# print(plakalar['istanbul'])  => 34

# plakalar = { 'kocaeli' : 41, 'istanbul': 34}

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)

users = {
    'salih': {
    'age': 27,
    'roles':['user'],
    'email': 'samethıhsfa@gmail.com',
    'address':'sakarya',
    'phone':'5535145'
    },
    'hacısalih':  {
    'age': 1,
    'roles': ['admin','user'],
    'email': 'samethfısfa@gmail.com',
    'address':'kocaeli',
    'phone':'5363824'
    }
}

print(users['hacısalih']['roles'][0])
