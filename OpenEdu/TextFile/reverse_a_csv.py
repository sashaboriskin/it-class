fin = open('input.csv', 'r')

for line in fin:
    a = line[:-1].split(';')
    a[0], a[1] = a[1], a[0]
    s = ';'.join(a)
    print(s)

fin.close()
