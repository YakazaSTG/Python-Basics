# Bankamatik Uygulaması


SametHesap = {
    'ad': 'Samet Gedik',
    'hesapNo': '12345678',
    'bakiye': 5000,
    'ekHesap': 3000
}

HasanHesap = {
    'ad': 'Hasan Berker',
    'hesapNo': '123551518',
    'bakiye': 3000,
    'ekHesap': 500
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar): 
        hesap['bakiye'] -= miktar 
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':           
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']}  bulunmaktadır.")
        else:
            print('Üzgünüz, Bakiyeniz Yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(SametHesap, 3000)


print('********************************')
paraCek(SametHesap, 5000)



