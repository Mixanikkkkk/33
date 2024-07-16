def function(x):
    for i in range(2, (int(x**0.5)+1)):
        if x%i==0:
            return False
    return True
f = open('171.txt')
russian_alphabet='QWERTYUIOPASDFGHJKLZXCVBNM'
numbers='1234567890'
t=0
c=0
auto_numbers=[str(i) for i in f]
for nomer in auto_numbers:
    if nomer[0] in russian_alphabet:
        t+=1
    if nomer[1] in numbers:
        t+=1
    if nomer[2] in numbers:
        t+=1
    if nomer[3] in numbers:
        t+=1
    if nomer[4] in russian_alphabet:
        t+=1
    if nomer[5] in russian_alphabet:
        t+=1
    if t==6:
        tsr = int(nomer[1:4])
        if ("FU" in nomer) and function(tsr)==True:
            c+=1
    t=0
print(c)
