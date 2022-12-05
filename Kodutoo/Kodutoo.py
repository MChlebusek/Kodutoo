
from math import *
#from random import *
#Töö "Vigade otsing -2"
print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a=(abs(int(input("Введите целое число => ")))) #lisatud sulud
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b>0: #käärsool
        if b%2==0: #lisatud võrdsed
            paaris+=1 #pomenjala znaki mestami
        else:
            paaritu+=1 #pomenjala znaki mestami
        b//=10 
    print("Чётных цифр:", paaris)
    print("Нечётных цифр:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0 
    while a>0: #lisatud võrdsed
        n=a%10 
        a=a//10 
        b=b*10 
        b+=n #pomenjala znaki mestami
    print("*Перевёрнутое* число", b) #eemaldas sulud
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
    if c%2==0:
       print(c, "- чётное число. Делим на 2.")
    else:
        print(c, " - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!=1:
        if c%2==0:
            c=c/2
        else:
            c=(3*c+1)/2
        print(int(c), end=" ") #lisas tsitaadi
    print()
    print("Гипотеза верна")





x=0
c=0
while x<10:
    x+=1
    while c<10:
        c+=1
        print(str(x*c).center(4), end="")
    c=0
    print()


for i in range(1,5):
    for o in range(1,5):
        print(str(i*o).center(4), end="")
    print()



#Напишите программу, печатающую столбик строк такого вида
for r in range(9):
    for c in range(9):
        if r==c:
            print(r+1, end=" ")
        else:
            print(0, end=" ")
    print()


print()


