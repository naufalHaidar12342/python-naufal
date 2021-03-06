def isEmpty():
    return L==[]

L=[]      
L.append('a') #menambahkan huruf a ke bagian top dari list/push a
L.append('b') #menambahkan huruf b ke bagian top dari list/push b
L.append('c') #menambahkan huruf c ke bagian top dari list/push c
print(L)
print(len(L))

L.pop() #hapus elemen paling atas (c)
L.pop() #hapus elemen paling atas (b)
print(isEmpty())
print(L)