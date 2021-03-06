#karena fungsi di list stack ternyata bisa digunakan juga di deque, maka kita coba semua fungsi tadi
from collections import deque
#buat stack deque kosong baru
mystack=deque()
def isEmpty():
    # return mystack==[]
    if len(mystack)==0: #modifikasi. karena 
        return True    #setelah dicoba, ketika kustomPop() lebih dari jumlah elemen, akan terjadi error
    else:               #solusi: ketika panjang stack sudah 0, mengembalikan True
        return False
    
def cetakDeque():
    print('data terbaru:',mystack)
    print('panjang stack:',len(mystack))
    print('is empty:',isEmpty())
    
def kustomPop():
    if not isEmpty():
        out=mystack.pop()
        print('data terhapus:',out)
        cetakDeque()
    else:
        print("stack empty cannot pop")
        

mystack.append('a')
mystack.append('b')
mystack.append('c')
print(mystack)
print('')
kustomPop()
print('')
kustomPop()
print('')
kustomPop()
print('')
kustomPop()

