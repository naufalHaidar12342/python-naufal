def isEmpty():
    return L==[]
	
L=[]
L.append('a')
L.append('b')
L.append('c')
print(L)

out=L.pop()

print('data terhapus :',out)
print('data terbaru :',L)
print('panjang stack :',len(L))

print(isEmpty())