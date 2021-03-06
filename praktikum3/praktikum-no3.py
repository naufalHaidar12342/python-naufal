def isEmpty():
    return L==[]

def cetakStack():
    print('data terbaru:',L)
    print('panjang stack:',len(L))
    print(isEmpty())
    
#membuat list L yang diatur dalam keadaan kosong
L=[]
L.append('a')
L.append('b')
L.append('c')
print(L)
print("") #memberi jarak / spasi saja

#pop elemen 'c'/hapus elemen
out=L.pop()
print('data terhapus:',out)
cetakStack()
print("") #memberi jarak / spasi saja

#pop elemen 'b'
out=L.pop()
print('data terhapus:',out)
cetakStack()
print("") #memberi jarak / spasi saja

#pop elemen 'a'
out=L.pop()
print('data terhapus:',out)
cetakStack()

#pop elemen apa ini?
# out=L.pop()
# print('data terhapus:',out)
# cetakStack()

#supaya tidak menimbulkan error karena menghapus elemen yang sudah tidak ada,kita menggunakan kondisi yang berkebalikan dengan isEmpty()
# contoh dengan if di file selanjutnya



