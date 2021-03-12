from math import pi

print ("Tugas 2 Praktikum Programa Komputer")
print ("Kalkulator luas dan suhu")

print ("Pilihlah salah satu yang akan anda hitung!")
print ("1. Luas Persegi Panjang")
print ("2. Luas Lingkaran")
print ("3. Luas Kubus")
print ("4. Konversi suhu Celcius ke Fahrenheit")
print ("5. Konversi Reamur ke Celcius")

cetak = 0
choice = input("Masukkan nomor pilihan anda : ")

if choice == "1":
    panjang = float(input("Masukkan panjang persegi : "))
    lebar = float(input("Masukkan lebar persegi: "))
    Luas = panjang*lebar

    print ("Luas persegi panjang adalah {}" .format(Luas))
    cetak = 1

elif choice == "2":
    rusuk = float(input("Masukkan jari-jari lingkaan : "))
    Luas = pi*rusuk*rusuk

    print ("Luas lingkaran adalah {}" .format(Luas))
    cetak = 1

elif choice == "3":
    rusuk = float(input("Masukkan rusuk kubus : "))
    Luas = 6*rusuk**2

    print ("Luas kubus adalah {}" .format(Luas))
    cetak = 1

elif choice == "4":
    celcius = float(input("Masukkan suhu celcius : "))
    celcius_ke_fahrenheit = (9/5 * celcius) + 32

    print ("suhu {} derajat celcius = {} derajat fahrenheit".format(celcius, celcius_ke_fahrenheit))
    cetak = 1

elif choice == "5":
    reamur = float(input("Masukkan suhu reamur : "))
    reamur_ke_celcius = 5/4 * reamur

    print ("suhu {} derajat reamur = {} derajat celcius".format(reamur,reamur_ke_celcius))
    cetak = 1

else :
    print("tidak tersedia")