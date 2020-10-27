'''
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите длину самой длинной последовательности, состоящей из
символов X. Хотя бы один символ X находится в последовательности.
'''

file = open('anjelica.txt', 'r')
max_x = 0
for line in file:
    counter_of_x = 0
    for letter in line:
        if letter == 'X':
            counter_of_x+=1
    if counter_of_x>max_x:
        max_x = counter_of_x

print(max_x)
file.close()
