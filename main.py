def tambah(num1, num2):
    return num1 + num2

def kurang(num1, num2):
    return num1 - num2

def kali(num1, num2):
    return num1 * num2

def bagi(num1, num2):
    if num2 == 0:
        print("Tidak bisa membagi dengan nol!")
    else:
        return num1 / num2



print("###### Kalkulator Sederhana ######")
print("Pilih Operasi Berdasarkan Nomor")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. pembagian (/)")

pilihan = input("Masukan Piihan Anda: ")

num1 = float(input("Masukan Angka Pertama: "))
num2 = float(input("Masukan Angka Kedua: "))


if pilihan == '1':
    print("Hasil: ", tambah(num1, num2))
elif pilihan == '2':
    print("Hasil: ", kurang(num1, num2))
elif pilihan == '3':
    print("Hasil: ", kali(num1, num2))
elif pilihan == '4':
    print("Hasil: ", bagi(num1, num2))
else:
    print("Operasi tidak valid")
    

