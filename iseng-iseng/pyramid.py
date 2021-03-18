angka1 = 1
angka2 = 1
baris = 5
count1 = 1
while angka1 < baris:
    out = ''.join((baris - angka1) * [' '])
    j = 0
    while j < angka1:
        out = '%s%s ' % (out, count1)
        j += 1
    print(out)
    out = ''
    angka1 += 1
