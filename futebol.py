import random
import time
from array import *


timesarr = []
i = 0
j = 0
k = 1


print("futibas simulator")
print("Quantos times você quer em seu campeonato?")




while True:
    times = input()
    try:
        val = int(times)
        print("O número de times será ", val)
        break
    except ValueError:
        print("Escolha um número natural, por favor")




while i < val:
    print("Escolha seu time " + str(i+1))
    timesarr.append(str(input()))
    i += 1




print("O campeonato foi criado! Vamos simular os jogos de todos contra todos!")
print("Ok, o jogo será entre: ")
while j < (val-1):
    while k < (val):
        if k != j:
            print("Ok, o jogo será entre: ")
            print(timesarr[j] + " vs " + timesarr[k])

            gols1 = 0
            gols2 = 0

            print("começou the game")

            i = 0
            atraso = 0.2

            while i <= 90:
                gay = random.randint(1,100)
                if(gay > 6):
                    print(i)
                elif(gay > 3):
                    print(str(i) + " gol do " + timesarr[j] + "!")
                    gols1 += 1
                elif(gay > 0):
                    print(str(i) + " gol do " + timesarr[k] + "!")
                    gols2 += 1
                i += 1
                time.sleep(atraso)




            print("o game acabou pai, lols")
            print("o jogo terminou:")
            print(timesarr[j] + " " + str(gols1))
            print(" vs ")
            print(timesarr[k] + " " + str(gols2))
            k += 1
    j+=1
























"""
print("escolha seu primeiro time")
time1 = input()
print("ok, o nome do seu time é " + time1)
print("escolha seu segundo time")
time2 = input()
print("ok, o nome do seu time 2 é " + time2)




print("Ok, o jogo será entre: ")
print(time1 + " vs " + time2)




gols1 = 0
gols2 = 0




print("começou the game")




i = 0
atraso = 0.2




while i <= 90:
    gay = random.randint(1,100)
    if(gay > 6):
        print(i)
    elif(gay > 3):
        print(str(i) + " gol do " + time1 + "!")
        gols1 += 1
    elif(gay > 0):
        print(str(i) + " gol do " + time2 + "!")
        gols2 += 1
    i += 1
    time.sleep(atraso)




print("o game acabou pai, lols")
print("o jogo terminou:")
print(time1 + " " + str(gols1))
print(" vs ")
print(time2 + " " + str(gols2))
"""


