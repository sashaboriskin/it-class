fin = open('input.txt', 'r')
unique_array_of_words = []
array_of_words = []

for line in fin:
    a = line.split()
    for word in a:
        array_of_words.append(word)

for i in array_of_words:
    if i not in unique_array_of_words:
        unique_array_of_words.append(i)
fin.close()

print(len(unique_array_of_words))

#answer - 79936
