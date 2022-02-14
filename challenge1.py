from os import environ
from webbrowser import get

getallen=[1,2,3,5,7,8,10,12,13,14,15,16,21,22,23,24,26,30,31,32,33,43,44,46,47]

nummer = len(getallen)
print(nummer)

evengetallen= 0
onevengetallen= 0
Boring= 0
for getal in getallen:
    if getal %2 == 0:
        evengetallen += 1
    else:
        onevengetallen += 1


print(evengetallen)
print(onevengetallen)
Boring = []
for i in range(len(getallen)):
    if i %2 == getallen[i] %2:
        Boring.append(getallen[i])

print(len(Boring))



