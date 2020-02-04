number = int(input("enter sourse number: "))
newnumber = 0
#если число пустое
if number == None:
  print("cannot work with such numbers, exiting")
  exit(0)

base = int(input("enter its base (2 <= base <= 9): "))

#проверка на допустимые цифры
for i in range(len(str(number))):
    if number[i] > base:
      print("illegal digit" + str(i) + "in a number with base" + str(base) + "," + "exiting")
      exit(0)

#если основание больше или меньше допустимого
if 1 > base > 9:
  print("cannot work with such bases, exiting")
  exit(0)

while(number !=0):
  newnumber = str(number%base) + newnumber 
  number //= base
