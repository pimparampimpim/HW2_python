
a=int(input())
f=1
s=1
#Ф=1 потому что это числитель для дробей а С=1 потумочто сложение идет по принципу(1+1/Н1...)
for i in range (1,a+1):
    #находим ту самую дробь 1/Н! первая ф=1 поэтому числитель константа(1) а мы все время елим т.е. умножаем знаменатель дроби 
    f=f/i
    s+=f
    #изначально сумма искалась по другому но внесены правки поэтому просто складываем значения дробей
    #ОКРУГЛЯЕМ
print (((s*100000)//1)/100000)