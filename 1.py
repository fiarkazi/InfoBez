import random
k=0
n=0
x=0
t=0
users=['admin', 'user1', 'user2', 'user3', 'user4', 'user5', 'user6']
files=['файл1', 'файл2', 'файл3', 'дисковод', 'CD-RW']
rights=['полные права', 'чтение', 'запись', 'передача прав', 'чтение, передача прав', 'чтение, запись', 'запись, передача прав', 'запрет']
m=[[0, 0, 0, 0, 0],
   [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)],
   [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)],
   [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)],
   [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)],
   [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)],
   [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7)]]
print(m)
u=str(input('User: '))
for i in range(0, 7):
    if u==users[i]:
        print('Идентификация прошла успешно, добро пожаловать в систему')
        n=i
    else:
        k=k+1
        i=i+1
    if k==7:
        print('Ошибка при вводе данных, повторите попытку позже')
if k==6:
    print('Перечень ваших прав:')
    for i in range(0, 5):
        x=m[n][i]
        print(files[i],':',rights[x])
    r=str(input('Жду ваших указаний > '))
    while r!='выход':
        f=int(input('Над каким объектом производится операция? > '))
        t=m[n][f-1]
        rt=rights[t]
        if r=='чтение' or r=='запись' or r=='передача прав':
            if r=='передача прав':
                o=str(input('Какое право передается? > '))
                s=str(input('Какому пользователю передается право? > '))
                if r in rt or rt=='полные права':
                    print('Операция прошла успешна')
                else:
                    print('Отказ в выполнении операции. У вас нет прав для ее осуществления')
            if r!='передача прав':
                if r in rt or rt=='полные права':
                    print('Операция прошла успешна')
                else:
                    print('Отказ в выполнении операции. У вас нет прав для ее осуществления')
        else:
            print('Такого действия не существует. Повторите попытку')
        r=str(input('Жду ваших указаний > '))
    print('Работа пользователя', u, 'завершена. До свидания.')
                    
        
    

    
