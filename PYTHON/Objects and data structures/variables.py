maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Değişken tanımlama kuralları

# rakam ile başlayamaz

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# büyük küçük harf duyarlılığı

age = 20
AGE = 30

print(age)
print(AGE)

#türkçe karakter kulanmayalım

yas = 20
_age = 20

x = 1             # int
y = 2.3           # float
name ="Samet"     # string
isStudent = False  # bool

#x, y, name, isStudent = (1, 2.3, "Samet", True)

a = '10'
b = '20' 
print(a+b) #30 => 1020

firstName = "Samet"
lastName = " Gedik"

print(firstName + lastName) # Samet Gedik