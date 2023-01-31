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