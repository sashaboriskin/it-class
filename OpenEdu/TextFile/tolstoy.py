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


for key in d:
    if key in string_of_bad_letters:
        del d[key]

print(d)
'''
for key, value in d.items():
    print(key, ' ', value, sep='')
'''
