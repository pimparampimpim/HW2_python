a=int(input())
s=1
#переменная для счетчика
for i in range(1,a):
#прокручиваем все числа от 1 до максимального числа меньше а
    if a%i==0:
#и подставляя сюда считаем количество делителей подпадающих под условие
        s+=1
print(s)
