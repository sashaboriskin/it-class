def hanoi(n, f1, t, f2):
  if n>0:
    if n>1:
      hanoi(n-1, f1, f2, t)
    print(f1, "-", t)
    if (n>1):
      hanoi(n-1, f2, t, f1)


n = int(input())
hanoi(n, 'A', 'B', 'C')
