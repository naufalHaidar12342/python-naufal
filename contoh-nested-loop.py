i=2 #menyatakan nilai i=2
while i<100: #ketika nilai i masih dibawah 100, akan diproses 
    j=2     #menyatakan nilai j=2
    while (j<=(i/j)): #loop ini akan berhenti jika nilai j lebih kecil atau sama dengan hasil i/j [ketika j=2 dan hasil i/j hasilnya lebih dari 1, maka tidak masuk ke while]
        if not (i%j) : #jika 0, berarti false
        j=j+1 #sebelumnya j bernilai 2. di baris ini ditambah 1 sehingga menghasilkan 3. dan seterusnya
    if j>i/j: #jika j yg bernilai 2 lebih besar dari i/j, maka akan mencetak i, dimana i masih bernilai 2
        print(i, "is prime")
        # print("show j=",j) #bagian tambahan untuk melacak perubahan nilai j
      
    i=i+1 #menambah nilai i dengan +1

print("good bye") #ketika i sudah bernilai lebih dari 99, bagian ini akan ditampilkan