Kmd=[]#tühi järjend

Km=10# 
print("1.paeval pikkus oli",Km)
Kmd.append(Km)
print(Kmd)
for p in range(2,8):
    Km*=1.1
    print(round(Km,2))
    Kmd.append(round(Km,2))
print(Kmd)
print(Kmd[2])
print(Kmd.index(16.11))
Kmd.remove(10)#pop(0)
Kmd.append(199)

print(Kmd)
print(Kmd.count(16.11))
print(len(Kmd))
