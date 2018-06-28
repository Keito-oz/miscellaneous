spam=0
while spam<6:
    print("Hi!")
    spam=spam+1

def hello():
    print("Howdy!")
    print("Howdy!")
    print("Hello there!")

def hello(name):
    print("Hello "+name+"!")

def spam():
    print(egg)
egg=42
spam()
print(egg)

def spam():
    global eggs
    eggs="spam"

eggs="global"
spam()
print(eggs)

def spam():
    print(eggs)
    eggs="spam local"

eggs="global"
spam()

def spam(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:
        print("Error!!!")

print(spam(0))
