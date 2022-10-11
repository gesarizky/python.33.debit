# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
volume = float(input("Tuliskan Berapa Volume Liter Air: "))
waktu = float(input("Tuliskan Berapa Jam Yang dibutuhkan: "))

# Mengkonversi
debit = volume / waktu

# Menampilkan Hasil
print('==========================================================')
print('Maka Debit Air = %0.2f Liter/Jam'  %(debit))
print('==========================================================')
