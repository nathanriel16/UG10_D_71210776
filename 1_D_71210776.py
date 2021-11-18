#Soal 1
makanan = int(input("Harga Makanan Sebesar : "))
snack = int(input("Harga Snack Sebesar : "))
minuman = int(input("Harga Minuman Sebesar : "))
uang = int(input("Uang Yang Anda Bawa Sebesar : "))

total = makanan + snack + minuman
utang = total - uang
kembalian = uang - total

print("Total yang harus anda bayar sebesar Rp", total)

if uang < total :
    print("Uang anda kurang! Anda memiliki utang sebesar Rp", utang)
elif uang == total :
    print("Uang anda pas! Tidak ada kembalian :D")
elif uang > total :
    print("Anda memiliki kembalian sebesar Rp", kembalian)