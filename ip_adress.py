#88.144.996.11 - bad
#192.168.5.12 - good
a = []
s = input() 
a = s.split('.')
result = 'Good'

for i in range(len(a)):
  if a[i] == '':
    result = 'Bad'

if result == 'Good':
  for i in range(len(a)):
    a[i] = int(a[i])

  for i in range(len(a)):
    if a[i] > 255:
      result = 'Bad'

print(result)
