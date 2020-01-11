#пока не доделано
fin = open('input (6).txt', 'r')
fout = open('otput (6).txt', 'w')
'''
How many:
1) letters
2) words
3) strings
'''
letters = 0
words = 0
strings = 0
print('Input file contains:', file=fout)
for line in fin:
    strings+=1
    array_of_words = line.split()
    for word in array_of_words:
        words+=1
        array_of_letters = word.split()
        for letter in array_of_words:
            if letter.isalpha() == True:
                letters+=1

print(letters, 'letters', file=fout)
print(words, 'words', file=fout)
print(strings, 'lines', file=fout)
fout.close()
fin.close()

#answer -
'''
Input file contains:
93203 letters
11000 words
1000 lines
'''
