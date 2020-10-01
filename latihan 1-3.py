#buat program untuk menghitung index massa tubuh / BMI (Body mass index)

def hitungBMI(tinggi,berat):
    tinggi = tinggi/100 #convert centimeter ke meter
    bmi = berat/(tinggi**2)
    return bmi
tinggi = int(input('Tinggi badan(cm) : '))#dalam centimeter
berat = int(input('Berat badan(kg) : '))
bmi = hitungBMI(tinggi,berat)
if bmi<18.5:
    print('Berat badan kurang')
elif bmi<23:
    print('Berat badan normal')
elif bmi<30:
    print('Berat badan berlebih(cenderung obesitas)')
elif bmi>=30:
    print('Obesitas')
