'''
Soal 1 - Time Converter (30 Poin)

Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").

    HH : Hours, 2 digits, range: 00 - 99

    MM : Minutes, 2 digits, range: 00 - 59

    SS : Seconds, 2 digits, range: 00 - 59

    Case Flow: Saat dieksekusi, program akan mencetak nilai return function.

Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, 
jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string 
akan keluar notifikasi. Invalid Input
'''

# Pseudo Code

# IF input <= 359999
# IF input > 359999 maka invalid input
# IF input == desimal maka invalid input
# IF input < 0 maka invalid input

# 1 jam = 3600 detik
# 1 menit = 60 detik


try:
    input_detik = int(input("masukan detik : "))
    if input_detik > 359999:
        print("input diluar jangkauan")
    elif input_detik < 0:
        print("input tidak menerima angka negatif")
    else:
        jam = int(input_detik//3600)
        modulus_jam = int(input_detik%3600)
        menit = int(modulus_jam//60)
        modulus_menit = int(modulus_jam%60)
        detik = int(modulus_menit%60)
        print("HH :","{0:0=2d}".format(jam),"|","MM :","{0:0=2d}".format(menit),"|","SS :","{0:0=2d}".format(detik))
except:
    print("format yang anda masukan salah")


#########################################################################



