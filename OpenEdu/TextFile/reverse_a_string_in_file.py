fin = open('input (3).txt', 'r')
output_stirng = ''
s = fin.readlines()
s.reverse()

for string in s:
    output_stirng= output_stirng + string + ' '
output_stirng = output_stirng[:-1]

fin.close()
print(output_stirng)
#answer - 
'''
The star appears stable, with little stellar variation.
than 10 times as much dust surrounding Tau Ceti as is present in the Solar System.
so is thought to be less likely to host rocky planets. Observations have detected more
from the Solar System, it is a relatively close star. Tau Ceti is metal-deficient and
although it has only about 78% of the Sun's mass. At a distance of just under 12 light years
Tau Ceti is a star in the constellation Cetus that is spectrally similar to the Sun,
'''
