#buat program untuk menentukan nilai maksimal dan minimal dari sejumlah nilai masukan N
jumlah_data = int(input('Jumlah data yang dimasukan : '))
data_list = []
for i in range(jumlah_data):
    data = int(input('Masukan data ke-{} : '.format(i+1)))
    data_list.append(data)
print()
nmin = data_list[0]
nmax = data_list[0]
for j in range(1,jumlah_data):
    if nmin>data_list[j]:
        nmin = data_list[j]
    if nmax<data_list[j]:
        nmax = data_list[j]
print('Nilai minimum =',nmin)
print('Nilai Maximum =',nmax)

