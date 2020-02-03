txt = ''
for i in range(1, 3):
    fin = open('Толстой Лев Николаевич. Война и мир. Книга ' + str(i) + '.txt', 'r')
    txt += fin.read()
    fin.close()

string_of_bad_letters = ""
d = {}
for symb in txt:
    if symb in d.keys():
        d[symb]+=1
    else:
        d[symb] = 1
print(d)

