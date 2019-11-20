#227654
n = 227654
s = str(n)
a = []
part_a_to_sort = []
part_a_before_sort = []
for i in range(len(s)):
  a.append(int(s[i]))

for i in range(len(a)-2,0,-1):

  if a[i] > a[i+1]:
    a[i], a[i+1] = a[i+1], a[i]
  else:
    part_a_to_sort = a[i+1:len(a)]
    part_a_before_sort = a[0:i+1]
    part_a_to_sort.sort() 
    a = part_a_before_sort + part_a_to_sort

print(a)
      
