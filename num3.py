from math import trunc
with open('travels.txt','r', encoding='utf-8-sig') as F:
    L_first=[0,0]
    L_second=[0,0]
    L_third=[0,0]
    List=[]
    weight_from_Lipki=0 #Груз из Липок
    distance_on_first_day=0 #Растояние в первый день
    D_of_send_cities={} #Словарь городов отправки
    D_of_take_cities={} #Словарь городов назначения
    D_of_fuel={} #Словарь для расчёта сред.расхода бензина 
    for i in F: 
        line = i.split()
        if line[0] == '1':
            L_first[0]+=1
            L_first[1]+=int(line[6])
            distance_on_first_day+=int(line[4]) #Растояние в первый день
        elif line[0] == '2':
            L_second[0]+=1
            L_second[1]+=int(line[6])
        else: 
            L_third[0]+=1
            L_third[1]+=int(line[6])

        if line[2]=='Липки':
            weight_from_Lipki+=int(line[6])

        if line[3] not in D_of_send_cities:
            D_of_send_cities[line[3]]=0 
            D_of_take_cities[line[3]]=0
            D_of_fuel[line[3]]=[0,0] #Сохрвнение в дикты городов отправления, назначения, и для расчёта сред. расхода бензина          

with open('travels.txt','r', encoding='utf-8-sig') as F:
    for i in F:
        line = i.split()
        D_of_send_cities[line[2]]+=int(line[6]) #Подсчёт масс грузов из пунктов отправления
        D_of_take_cities[line[3]]+=int(line[6]) #Подсчёт масс грузов из пунктов назначения
        D_of_fuel[line[3]]=[D_of_fuel.get(line[3])[0]+1 ,D_of_fuel.get(line[3])[1]+int(line[5])] #Добавление в дикт значений расстояние до пунктов назначения и расход бензина
        
for i in D_of_fuel:
    values = D_of_fuel[i]
    D_of_fuel[i]=round(values[1]/values[0],2)

Max=[0,0] #Список для определения максимума
for i in D_of_fuel:
    if D_of_fuel[i]>Max[1]:
        Max=[i,D_of_fuel[i]]
          
print(f'first day--{L_first}, second day--{L_second}, third day--{L_third}')
print(f'Масса грузов из Липок--{weight_from_Lipki}') 
print(f'Суммарное растояние за 1 октября--{distance_on_first_day}')
print(f'Пункты отправления--{D_of_send_cities}--всего пунктов--{len(D_of_send_cities.keys())}')
print(f'Пункты назначения--{D_of_take_cities}--всего пунктов--{len(D_of_take_cities.keys())}')
print(f'Пункт назначения с нибольшим сред. расходом бензина--{Max[0]}--{Max[1]}')
