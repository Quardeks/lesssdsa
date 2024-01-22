start = 1970#input('start')
stop = 1975#input('stop')
k=0
with open('task1.txt', 'r',encoding="utf-8") as F:
    for i in F:
        names = i.split()
        age = i.split(sep=('.'))
        if int(age[2])<1978:
            k+=1
            print (names[0],age[2],k)
with open('task1.txt','r',encoding='utf-8')as F:
    for i in F:
        age = i.split(sep=('.'))
        if int(age[2])>=start and int(age[2])<=stop:
            print(i)
