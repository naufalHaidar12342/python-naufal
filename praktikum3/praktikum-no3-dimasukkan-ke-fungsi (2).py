def isEmpty():
    return L==[]
    
def cetakStack(L):
    print('data terbaru:',L)
    print('panjang stack:',len(L))
    print(isEmpty())
    
def customPop(L):
    if not isEmpty():
        out=L.pop()
        print('data terhapus:',out)
        cetakStack(L)
    else:
        print("list empty cannot pop")
        
#buat list L yang awalnya kosong        
L=[]
L.append('a')
L.append('b')
L.append('c')
print(L)
print('')
customPop(L)
print('')
customPop(L)
print('')
customPop(L)