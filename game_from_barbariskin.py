import random

'''
number - загаданное число
number_of_attempts - число попыток
attempt - попытка
'''

number = random.randint(0, 10)
number_of_attempts = 5 
print("угадайте число от 0 до 10")
i = 0

while i < number_of_attempts:  
  attempt = int(input('новая попытка: '))
  if attempt > number:
    print("меньше")
    i += 1
  elif attempt < number:
    print("больше")
    i += 1
  else:
    print("угадано!")
    print(i + 1, "Попыток было затрачено")
    break
else:
  print("провал((( чел ты...")
