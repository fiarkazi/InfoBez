import  random
import math
import time
P=10**(-4)
T=15
V=3*60*24*(T/7)
SS=math.ceil(V*(T/7)/P)
print("Нижняя граница S*: ",SS)
A=1
p=""
n=""
M=""
L=int(input("Введите длину пароля "))
while (SS>=(A**L)):
    A=A+1
A=A-1
for i in range(33, 127):
    M=M+chr(i)
#print(M)
k=random.randint(0, 93)
m=M[k]
c=1
u=1
h=0
while u<A:
    k=random.randint(0, 93)
    for j in range(0, c):
        if M[k]!=m[j]:
            h=h+1
    if h==c:
        m=m+M[k]
        u=u+1  
    c=len(m)
    h=0
  #print('**************')
#print('----------------------------------------------------')
print(m)    
for i in range(0, L):
    c=random.choice(m)
    p=p+c
     
print("Мощность алфавита: ", A)
print("Генерируемый пароль, длиной" , L, "равен ", p)
x=input("Запустить процедуру перебора паролей (y/n): ")

if (x=="y"):
    print("Примерное время перебора", int(T*24), "часов")
    print("Скорость перебора", 3*60, "паролей в час")
    print("Для выхода из цикла нажмите Ctrl+c")
    time.sleep(3)
    T=T*24*60*60
    while(p!=n):
        n=""
        for j in range(0, L):
            c=random.choice(m)
            n=n+c
        print(n)
        T=T-1
        print("Примерное время перебора",int((T)),"секунд")
         



