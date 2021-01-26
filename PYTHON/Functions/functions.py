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

ageSamet = yasHesapla(2004)
ageHasan = yasHesapla(2005)
ageKeremali = yasHesapla(2008)

print(ageSamet, ageHasan, ageKeremali)

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

EmekliligekacYilKaldi(1961, 'besim')
EmekliligekacYilKaldi(1957, 'Ali')
EmekliligekacYilKaldi(1978, 'Muhammet')

print(help(EmekliligekacYilKaldi))

list = [1,2,3]

print(help(list.append))