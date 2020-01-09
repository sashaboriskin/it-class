x = int(input())
y = int(input())
all_money = (x*100+y)*2
rubles = all_money//100
kopeyki = all_money-(rubles*100)
print(rubles, kopeyki)
