# name = 'Samet Gedik'

# for letter in name:
#     if letter == 'G':
#             continue
#     print(letter)

# x = 0

# while x < 5:
#     x+=1
#     if x == 2:
#         continue
#     print(x)


# 1-100 e kadar tek sayıalrın toplamı

x = 0
result = 0


while x <= 100:
    x+=1
    if x % 2 == 0:
        continue
    result += x
    

print(f'toplam: {result}')