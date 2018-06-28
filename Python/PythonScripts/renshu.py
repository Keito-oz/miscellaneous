PATH追加
path C:\Users\ozaw0540\AppData\Local\Programs\Python\Python36-32

CD移動
cd C:\Users\ozaw0540\AppData\Local\Programs\Python\Python36-32\code

tokyo_temps=[15.1,15.4,15.2,15.4,17.0,16.9]

tokyo_temps[5]-tokyo_temps[0]

e_tokyo_temps=[13.6,13.5,14.2,14.8,14.8]

tokyo_temps2=e_tokyo_temps+tokyo_temps

tokyo_temps[1:2]
"""コメントが書けます"""
#これもコメントです

city_temps=[
    [14.8,14.8,15.0,15.4,15.2,15.4,17.0,16.9],
    [10.0,10.4,11.5,11.2,10.9,10.6,11.8,12.2],
    [16.0,15.5,15.9,16.4,15.9,15.6,17.5,17.1]
    ]

city_temps[1]

sum(city_temps[1])
max(city_temps[2])
min(city_temps[0])
len(city_temps[1])
average=sum(city_temps[1])/len(city_temps[1])

mus =["1!","2!","3!","4!","5!","6!","7!","8!","9!"]
for member in mus:
    print(member)

import numpy as np


#標準偏差の計算
monk_fish_team=[158,157,163,157,145]

total=sum(monk_fish_team)
length=len(monk_fish_team)
mean=total/length
variance=0

for height in monk_fish_team:
    variance+=(height-mean)**2

variance=variance/length
variance

std=variance**0.5

#range()を用いた繰り返し
for cnt in range(10):
    print(cnt)

#複利の計算
savings=100
rate=0.05
for i in range(15):
    savings+=savings*rate

savings

if 2*2*2+2==10:
    print(2*2*2+2)

if 2+2*2+2==10:
    print(2+2*2+2)

if (2+2)*2+2==10:
    print((2+2)*2+2)

if 1==1:
    print("1番目はTrue")

if 5^(4-4)+9==10:
    print("2番目はTrue")

if 2<len([0,1,2]):
    print("3番目はTrue")

if sum([1,2,3,4])<10:
    print("4番目はTrue")

if "AUG"=="AUG":
    print("True")

    
if "AUG"=="aug":
    print("True")

    
if "あい"=="あい":
    print("True")


if "GAG" in "GAGAAadhaoDAESA":
    print("あるよ")

if 2 in [1,2,3,4,5,6,0]:
    print("True!")

if [1,2] in [1,2,3,4,5,6,0]:
    print("True!")


if [1,2] in [[1,2],3,4,5,6,0]:
    print("True!")


if 2**3-2+4==10:
    print("10になる")
else:
    print(" 10にならない")

a_year=2080
if a_year>=1989:
    if a_year==1989:
        print(a_year,"年Oz誕生")
    else:
        print(a_year,"年Oz",a_year-1989,"歳")


if a_year==1989:
    print(a_year,"年Oz誕生")
elif a_year>1989:
    print(a_year,"年Oz",a_year-1989,"歳")
elif a_year<1989:
    print("Oz誕生まであと",1989-a_year,"年")


a_num=59

for num in range(2,a_num):
    if a_num % num==0:
        print("Not Prime")
        break


list=[123,456,789]
summary=0
for item in list:
    summary=summary+item

summary

def destiny_utility():
    utility=["IARA","CARA","DARA"]
    num=input("好きな数字を入れてください")
    idx=int(num)%len(utility)
    print("あなたの効用関数は")
    print(utility[idx],"です")

destiny_utility()


def destiny_utility2(num):
    utility=["IARA","CARA","DARA"]
    idx=num%len(utility)
    print("あなたの効用関数は")
    print(utility[idx],"です")

num_str=input("好きな数字を入れてください")
num=int(num_str)
destiny_utility2(num)


from random import randint
num=randint(0,10)
destiny_utility2(num)



def destiny_utility3(num):
    utility=["IARA","CARA","DARA"]
    idx=num%len(utility)
    return utility[idx]

from random import randint
num=randint(0,10)
u=destiny_utility3(num)
print("あなたの効用関数は",u,"です")


#local変数を関数の外で使うと？
def test_func(arg1):
    inner_var=100
    print(arg1+inner_var)


test_func(10)
inner_var

#標準偏差の計算
def calc_variance(a_list):
    total=sum(a_list)
    length=len(a_list)
    mean=total/length
    variance=0

    for height in a_list:
        variance+=(height-mean)**2
    variance=variance/len(a_list)

    return variance

