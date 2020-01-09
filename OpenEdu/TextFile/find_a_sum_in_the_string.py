fin = open('input (2).txt', 'r')
array_of_sums = []
string_of_sums = ''
for line in fin:
    sum = 0
    string_of_numbers = line.split()
    for number in string_of_numbers:
        sum+=int(number)
    array_of_sums.append(sum)

for i in array_of_sums:
    string_of_sums = string_of_sums + str(i) + ' '

string_of_sums = string_of_sums[:-1]
fin.close()

print(string_of_sums)

#answer - 34568147 255016 5617498 0 31397 17 10119996 111
