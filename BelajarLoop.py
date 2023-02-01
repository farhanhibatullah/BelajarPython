#while loop
n = 10
while n > 0:
    print(n)
    n = n - 1
print("mulai")

#for loop
n = [1,1,1,1,2,1,1,1]
indeks = [0,1,2,3,4,5,6,7]

for x in indeks:
    print("indeks ke-", indeks[x], "angkanya adalah ", n[x])
print("jumlah angka 1 di dalam list adalah ", n.count(1))

#latihan freecodecamp.org

#mencari nilai terbesar dan terkecil

n = [34, 20, 9, 17, 6, 2, 100, 101, 103, 99, 98, 97, 102, -1, 0, -100]

#metode pencarian nilai terbesar

max_num = None
print("Before: nilai terbesar saat ini adalah", max_num)
for x in n:
    if max_num is None or x > max_num:
        max_num = x
    print(max_num, x)
print("After: nilai terbesar saat ini adalah ", max_num)

#metode pencarian nilai terkecil

min_num = None
print("Before: nilai terkecil saat ini adalah", min_num)
for y in n:
    if min_num is None or y < min_num:
        min_num = y
    print(min_num, y)
print("After: nilai terbesar saat ini adalah ", min_num)

#buat penjumlahan dengan perulangan dan percabangan
#tampilkan pesan error "Invalid Input" menggunakan try and except

jumlah_iterasi = 0
total = 0

#proses perulangan
while True:
    nilai = input("masukkan nilai = ")
    #proses percabangan
    if nilai == 'done':
        print("selesai")
        break
    
    #proses try (Menangkap dan memeriksa input User)
    try:
        float_nilai = float(nilai)
    
    #proses yang akan ditampilkan apabila terjadi error
    except:
        print("Invalid Input")
        continue    #sintaks yang digunakan untuk melanjutkan perulangan
    
    print(float_nilai)
    jumlah_iterasi = jumlah_iterasi + 1
    total = total + float_nilai

print("Total nilai adalah = ", total)
print("Jumlah input yang dimasukkan = ", jumlah_iterasi)
print("Hasil bagi total dan jumlah input = ", total/jumlah_iterasi)
    
