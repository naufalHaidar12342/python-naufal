def isEmpty():
    return L==[]

def cetakStack(L):
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
if not isEmpty():
    out=L.pop()
    print('data terhapus:',out)
    cetakStack(L)
    print("") #memberi jarak / spasi saja

#pop elemen 'b'
if not isEmpty():
    out=L.pop()
    print('data terhapus:',out)
    cetakStack(L)
    print("") #memberi jarak / spasi saja
else:
    print("list empty cannot pop")

#pop elemen 'a'
if not isEmpty():
    out=L.pop()
    print('data terhapus:',out)
    cetakStack(L)
else:
    print("list empty cannot pop")
    
#pop elemen apa ini?
if not isEmpty():
    out=L.pop()
    print('data terhapus:',out)
    cetakStack(L)    
else:
    print("list empty cannot pop")