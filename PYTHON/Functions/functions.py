# fonksiyon

def sayHello(name = 'user'):
    return 'Hello'+ name

msg = sayHello('Samet')
msg = sayHello('Gedik')

print(msg)

def total(num1 , num2):
    return num1 + num2

result = total(10,20)  
result = total(15,20)    
print(result)

def yasHesapla(dogumYili):
    return 2020 - dogumYili

ageMehmet = yasHesapla(1999)
ageHasan = yasHesapla(2005)
ageAli = yasHesapla(2008)

print(ageMehmet, ageHasan, ageAli)

def EmekliligekacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

EmekliligekacYilKaldi(1960, 'Mehmet')
EmekliligekacYilKaldi(1957, 'Ali')
EmekliligekacYilKaldi(1977, 'Ahmet')

print(help(EmekliligekacYilKaldi))

list = [1,2,3]

print(help(list.append))
