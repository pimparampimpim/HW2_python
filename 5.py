otv=1
p=0
while True:
    a=int(input())
    if a==0:
        break  
    if a==p:
        otv+=1
    if a>p:
        p=a
        otv=1
print(otv)