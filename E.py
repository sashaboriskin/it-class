s = input()
new_s = ''
for i in range(len(s)):
  if s[i]!='4' and s[i]!='7':
    new_s = new_s + s[i]

print(new_s)
