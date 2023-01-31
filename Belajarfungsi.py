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
    x = 0
    while x != jum_char:
        print("index ke-", x, " hurufnya adalah ", kata[x])
        x = x+1
    spasi = kata.count(' ') 
    print("jumlah spasi adalah ", spasi)
    print("jumlah karakter yang ada pada kata ini adalah = ", jum_char) 
    print("jumlah huruf dalam kata adalah = ", jum_char - spasi)
    
    
pengulangan_kata(input("masukkan kata = "))


#latihan dari freecodecamp.org

sh = input("\nenter hours: ")
sr = input("enter rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40 :
	reg = fr * fh
	otp = (fh - 40.0) * (fr * 0.5)
	xp = reg + otp
else :
	xp = fr * fh
print("Pay:", xp)

#ubah ke fungsi computepay(hours, rate)

def computepay(hours, rate):
    fl_hours = float(hours)
    fl_rate = float(rate)
    if fl_hours > 40:
        reg = fl_hours * fl_rate
        otp = (fl_hours - 40.0) * (fl_rate * 0.5)
        xp = reg + otp
    else : 
        xp = fl_hours * fl_rate
    print("Pay:", xp)
    
computepay(45, 10)
