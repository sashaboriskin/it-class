#encoding='cp1251' - ?
txt = ''
for i in range(1, 3):
    fin = open('Толстой Лев Николаевич. Война и мир. Книга ' + str(i) + '.txt', 'r')
    txt += fin.read()
    fin.close()

string_of_bad_letters = ",.;:/_!«»-–?()’…;*„“—№=°"
array_of_bad_letters = [' ', '\n', '\xa0', '\t', ]
d = {}

for symb in txt:
    if symb in d.keys():
        d[symb]+=1
    else:
        d[symb] = 1

newdic = d.copy()

for key in newdic:
    if key in string_of_bad_letters:
        del d[key]
    elif key in array_of_bad_letters:
        del d[key]

for key, value in sorted(d.items(), key=lambda para: para[1], reverse=True):
    print(key, ' ', value, sep='')
