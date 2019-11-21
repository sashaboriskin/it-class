'''
12 ==> 21
513 ==> 531
2017 ==> 2071

9 ==> -1
111 ==> -1
531 ==> -1
'''
n = 227654
s = str(n)
a = []
part_a_to_sort = []
part_a_before_sort = []
for i in range(len(s)):
  a.append(int(s[i]))
was_break =0
for i in range(len(a)-2,-1,-1):
  if a[i] < a[i+1]:
    a[i], a[-1] = a[-1], a[i]
    part_a_to_sort = a[i+1:len(a)]
    part_a_before_sort = a[0:i+1]
    part_a_to_sort.sort() 
    a = part_a_before_sort + part_a_to_sort
    was_break = 1
    break
  
if was_break:
  print(a)
else:
  print(-1)
