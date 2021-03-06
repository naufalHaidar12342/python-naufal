from collections import deque

#stack kosong dengan mode deque (double pointer)
mystack=deque()

#menambahkan elemen ke deque
mystack.append('a')
mystack.append('b')
mystack.append('c')
print(mystack)

#hapus elemen
out=mystack.pop()
print(out)
print(mystack)