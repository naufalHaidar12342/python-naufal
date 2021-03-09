# langkah pertama, kita insialisasi/ define
# bagian yang konstan, seperti biaya admin bank
# dan kelipatan transaksi yang minimal 50 ribu

admin_bank = 5000
min_transaksi = 50000

# mencetak keterangan awal, seperti min. saldo
# dan biaya admin bank
print("Minimal saldo untuk penarikan adalah Rp. 50.000,00")
print("termasuk biaya administrasi sebesar Rp. 5.000,00")

# meminta input dari user
tarik_tunai = int(input(">>>>masukkan saldo yang akan ditarik = "))
# print("") berguna untuk menghasilkan baris kosong
# biasanya kita gunakan sebagai pemberi jarak
print("")

# tanda (%) bernama modulo, biasa disingkat mod
# artinya hasil sisa bagi

# jika tarik_tunai dibagi dengan min_transaksi
# dan sisa pembagiannya itu 0, maka lakukan
# perintah di bawahnya if statement
if tarik_tunai % min_transaksi == 0:
    saldoPenarikan = tarik_tunai-admin_bank
    print("==========TRANSAKSI BERHASIL==========")
    print(">>>>> Saldo ditarik = Rp.{}".format(tarik_tunai))
    print(">>>>> Biaya adm = Rp.{}".format(admin_bank))
    print(">>>>>>>Total = Rp.{}".format(saldoPenarikan))

# bagian ini kebalikan dari kondisi atasnya
# jika sisa pembagian bukan 0, maka jalankan
# perintah di bawah elif
elif tarik_tunai % min_transaksi != 0:
    print("==== Maaf, saldo untuk penarikan harus kelipatan Rp. 50.000,00 ====")

else:
    print("==== Maaf, saldo minimal untuk penarikan tidak cukup ====")
