prime={2,3,5,7,11,13,17}
fib={1,1,2,3,5,8,13}

prime_fib=prime|fib
prime_fib

prime_fib=prime&fib
if 13 in prime_fib:
    print("13は素数かつフィボナッチ数")
if {2,3} <= prime_fib:
    print("2,3は素数かつフィボナッチ数")

dice={1,2,3,4,5,6}
even={2,4,6}

odd_dice=dice-even
odd_dice

pf=prime&fib

pf_xor=prime^fib

list=["IARA","CARA","DARA","CARA","dara"]
s_list=set(list)

month_name=("Jan","Feb","Mar","Apr","May","Jun","Jul")
month_name2=("Aug","Sep","Oct","Nov","Dec")
month_name_year=month_name+month_name2

#タプルはディクショナリのキーに出来る
coordinate={(1,1):"A",(1,2):"B",(2,1):"C"}
xy=(2,1)
for co in coordinate:
	if xy==co:
		print(coordinate[co])
		break

for key in coordinate:
    dist=(xy[0]-key[0])**2+(xy[1]-key[1])**2
    if nearest_dist>dist:
        nearest_dist=dist
        nearest_point=coordinate[key]

while cnt <=100:
    if cnt%3==0 and cnt%5==0:
        print("FizzBuzz")
    elif cnt%3==0:
        print("Fizz")
    elif cnt%5==0:
        print("Buzz")
    else:
        print(cnt)
    cnt+=1

from random import randint
>>> hands={0:"グー",1:"チョキ",2:"パー"}

>>> rules={(0,0):"あいこ",(0,1):"勝ち",(0,2):"負け",
       (1,0):"負け",(1,1):"あいこ",(1,2):"勝ち",
       (2,0):"勝ち",(2,1):"負け",(2,2):"あいこ"}

while True:
    pc_hand=randint(0,2)
    user_hand_str=input("0:グー 1:チョキ 2:パー 3:やめる")
    if user_hand_str=="3":
        break
    if user_hand_str not in ("0","1","2"):
        continue
    user_hand=int(user_hand_str)
    print("あなた:"+hands[user_hand]+", コンピュータ:"+hands[pc_hand])

    print(rules[(user_hand,pc_hand)])


for num in range(2,a_num):
    if a_num % num==0:
        print("Not Prime")
        break
else:
    print(a_num," is a prime.")

def fizzbuzz(count=100,fizzmod=3,buzzmod=5):
    for cnt in range(1,count+1):
        if cnt%fizzmod==0 and cnt%buzzmod==0:
            print("FizzBuzz")
        elif cnt%fizzmod==0:
            print("Fizz")
        elif cnt%buzzmod==0:
            print("Buzz")
        else:
            print(cnt)


local_var=1

def test_func(an_arg):
    local_var=an_arg
    print("test_finc()の中=",local_var)

print("test_func_()の外=",local_var)


alphabet=["A","B","C","D","E"]
alphabet.index("A")

str="いっぱい"
str.replace("い","お")

str_num="1,000,000"
num=int(str_num.replace(",",""))

import matplotlib.pyplot as plt

str_speeds="38 42 20 40 39"
str_armor="80 50 17 50 51"
speeds=str_speeds.split(" ")
armors=str_armor.split(" ")
markers=["o","v","^","<",">"]

for idx in range(len(speeds)):
    x=int(speeds[idx])
    y=int(armors[idx])
    plt.scatter(x,y,marker=markers[idx])

plt.show()

speeds=str_speeds.split()
csep_speeds=",".join(speeds)

from math import pi
pi()

def func():
    words="""ABC,
DEF"""
    print(words)

func()

