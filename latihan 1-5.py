#buat program untuk menentukan validasi username dan password,
#dimana akan di ulang maksimal 3 kali,
#jika benar akan muncul komentar ” anda berhasil masuk”
#tapi jika tidak muncul komentar ” maaf user name dan password anda salah”

username = input('Username : ')
password = input('Password : ')
cek = False
batas = 0
print()
while not cek and batas<3 :
    print('Masukan kembali username dan password')
    un = input('Username : ')
    pw = input('Password : ')
    print()
    if un==username and pw==password:
        cek = True
        print('anda berhasil masuk')
    else:
        print('maaf user name dan password anda salah')
    print()
