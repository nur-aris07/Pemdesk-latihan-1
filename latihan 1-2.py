#buat program menghitung luas dan keliling bangun datar 
#  dengan menerima inputan dari user
import math
def Persegi():
    s = int(input('Nilai sisi : '))
    luas = s*s
    keliling = 4*s
    return luas,keliling
def PersegiPanjang():
    p = int(input('Nilai panjang : '))
    l = int(input('Nilai lebar : '))
    luas = p*l
    keliling = 2*(p+l)
    return luas,keliling
def SegitigaSiku():
    a = int(input('Nilai alas : '))
    t = int(input('Nilai tinggi : '))
    luas = (a*t)/2
    keliling = math.sqrt((a**2 + t**2)) + a +t
    return luas,keliling
def SegitigaKaki():
    a = int(input('Nilai alas : '))
    t = int(input('Nilai tinggi : '))
    luas = (a*t)/2
    s = math.sqrt(((a/2)**2 + t**2))
    keliling = a+(2*s)
    return luas,keliling
def JajarGenjang(a,b,t):
    a = int(input('Nilai alas : '))
    b = int(input('Nilai miring : '))
    t = int(input('Nilai tinggi : '))
    luas = a*t
    keliling = 2*(a+b)
    return luas,keliling
def menu():
    print('Pilih salah satu bangun datar di bawah ini :')
    print('1. Persegi')
    print('2. Persegi Panjang')
    print('3. Segitiga Siku-siku')
    print('4. Segitiga Sama Kaki')
    print('5. Jajar Genjang')
    bangun_datar = int(input('>> '))
    return bangun_datar
print('======= Menghitung Luas dan Keliling Bangun Datar =======')
print()
bangun_datar = menu()
print()
if bangun_datar==1:
    luas,keliling = Persegi()
elif bangun_datar==2:
    luas,keliling = PersegiPanjang()
elif bangun_datar==3:
    luas,keliling = SegitigaSiku()
elif bangun_datar==4:
    luas,keliling = SegitigaKaki()
elif bangun_datar==5:
    luas,keliling = JajarGenjang()
print('Maka bangun datar tersebut memiliki nilai luas =',luas,'dan nilai keliling =',keliling)
