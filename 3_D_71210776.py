#Soal 3
daftar = str(input("Masukkan daftar belanja anda : "))
print("Daftar Belanja : ", daftar.title().split())

daftartambah = input("Masukkan barang yang ingin ditambahkan : ")
hasil = daftar.title() + " " + daftartambah.upper()
if daftartambah in daftar :
    print("Barang", daftartambah.upper(), "sudah berada dalam daftar belanja.")
else :
    print("Hasil penambahan pada daftar belanja : ", hasil.split())