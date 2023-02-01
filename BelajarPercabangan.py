print("Program konversi nilai biner ke desimal")

print("apakah Anda ingin melakukan konversi?")
jawab = input("Jawab = ")

while True:
    if jawab == 'ya' or jawab == "Ya":
        biner = int(input("masukkan nilai biner = "))
        angka_desimal = 0
        i = 1
        while biner != 0:
            nilai_sisa = biner % 10
            angka_desimal = angka_desimal + (nilai_sisa*i)
            i = i * 2
            biner = biner // 10
        print(angka_desimal)
        
        print("apakah anda ingin keluar?")
        jawab_keluar = input("Jawab = ")
        if jawab_keluar == 'ya' or jawab_keluar == 'Ya':
            break
        elif jawab_keluar == 'tidak' or jawab_keluar == 'Tidak':
            continue

    elif jawab == 'Tidak' or jawab == 'tidak':
        break

    else:
        print("jawaban yang anda masukkan salah")
        break
    

