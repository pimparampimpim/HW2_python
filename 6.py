
a=int(input())
f=1
s=1
for i in range (1,a+1):
    f=f/i
    s+=f
print (((s*100000)//1)/100000)