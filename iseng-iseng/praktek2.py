# langkah pertama, kita minta input dari user
# huruf n bisa diganti nama lain
n = int(input("masukkan angka sembarang ="))

# seperti biasa, print("") untuk menghasilkan baris kosong
print("")

# supaya bisa dihitung digitnya
# angka tersebut kita ubah ke string dulu
ubahKeStr = str(n)

# fungsi len [length] menghitung panjang string
panjangAngka = len(ubahKeStr)

# yang akan dipanggil adalah "n" dan
#  "panjangAngka"
if len(ubahKeStr) == 1:
    print("angka {} terdiri dari {} digit".format(n, panjangAngka))

elif len(ubahKeStr) == 2:
    print("angka {} terdiri dari {} digit".format(n, panjangAngka))

elif len(ubahKeStr) == 3:
    print("angka {} terdiri dari {} digit".format(n, panjangAngka))

else:
    print("angka {} terdiri dari {} digit".format(n, panjangAngka))
