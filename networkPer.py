import random

def time1():
    n = int(input())
    total = average = 0
    for i in range(n):
        rand = random.uniform(0, 20)
        if rand < 5:
            total += 1
    average = total/n * 100
    print(str("%.2f"%average) + "%")
    
def time2():
    n = int(input())
    total = average = 0
    for i in range(n):
        rand = random.uniform(0, 20)
        total += 20 - rand
    average = total/n
    print(str("%.2f"%average) + " นาที")
    
def time3():
    n = int(input())
    total = average = 0
    for i in range(n):
        rand = random.uniform(0, 140)
        if 5 <= rand <= 20:
            total += 1
        elif 40 <= rand <= 60:
            total += 1
        elif 75 <= rand <= 100:
            total += 1
        elif 110 <= rand <= 140:
            total += 1
    average = total/n * 100
    print(str("%.2f"%average) + "%")
    
def time4():
    n = int(input())
    total = average = 0
    for i in range(n):
        rand = random.uniform(0, 140)
        w = 0
        if rand <= 20:
            w = 35 - rand
        elif 20 < rand <= 60:
            w = 70 - rand
        elif 60 < rand <= 100:
            w = 105 - rand
        else:
            w = 140 - rand
        total += w
    average = total/n
    print(str("%.2f"%average) + " นาที")

time1()
time2()
time3()
time4()
