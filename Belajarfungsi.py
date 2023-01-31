print("ini fungsi tanpa parameter")

def penjumlahan():
    print("ini fungsi penjumlahan")

penjumlahan()

print("\nini fungsi dengan parameter")
def penjumlahan(nilai):
    if nilai == True:
        print("ini fungsi penjumlahan")
    else:
        print("ini bukan fungsi penjumlahan")
        
penjumlahan(True)
penjumlahan(False)
penjumlahan(0)

print("\nini fungsi tanpa parameter dengan return value")

x = int(input("masukkan nilai = "))
y = int(input("masukkan nilai = "))

def penjumlahan():
    nilai1 =  x
    nilai2 = y 
    return print("ini hasilnya", nilai1+nilai2)

penjumlahan()

print("\nini fungsi dengan parameter dan return value")

def penjumlahan(x, y):
    nilai1 =  x
    nilai2 = y 
    return print("ini nilainya ", nilai1 + nilai2)

penjumlahan(20,30)
penjumlahan(100, 50)
penjumlahan(10, 10)
penjumlahan(100, 50.0)
penjumlahan(76.5 , 50.0)


def pengulangan_kata(kata):
    jum_char = len(kata)
    hitung = int(jum_char)
    x = 0
    while x != jum_char:
        print("index ke-", x, " hurufnya adalah ", kata[x])
        x = x+1
    print("jumlah karakter yang ada pada kata ini adalah = ", jum_char)
        
    
pengulangan_kata(input("masukkan kata = "))