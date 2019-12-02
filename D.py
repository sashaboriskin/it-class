n = int(input())
s = 0
n = str(n)

for i in range(len(n)):
  if n[i]=='0':
    s+=1
print(s)
