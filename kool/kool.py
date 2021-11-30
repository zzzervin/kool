#Kmd=[]#tühi järjend

#Km=10# 
#print("1.paeval pikkus oli",Km)
#Kmd.append(Km)
#print(Kmd)
#for p in range(2,8):
    #Km*=1.1
    #print(round(Km,2))
    #Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11))
#Kmd.remove(10)#pop(0)
#Kmd.append(199)
#print(Kmd)
#print(Kmd.count(16.11))
#print(len(Kmd))

#Maakonnad=["Tallin","Narva","Narva-jõusu","Kahla-Jarve","Ida-Viruma, Lääne-Virumaa, Jõgevamaa","Lääneituma","Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
#    try:
#        Index=int(input())
#        if len(str(Index))==5:
#            break
#    except ValueError:
#        print("ei")
#i_list=list(str(Index))
#s1=int(i_list[0])#1->0,2->1
#print(str(Maakonnad[s1-1]))
#if s1 in[1,2,3]:
#    print("Jatke kodus!")
#else:
#     print("Kanna maski")


#from random import*
#spisok=[]
#N=int(input("N"))
#for i in range(N):
#    spisok.append(randint(1,100))    
#print(spisok)
#L1=spisok[0]
#L2=spisok[-1]
#spisok.pop(0)
#spisok.insert(0,L2)
#print(spisok)


from random import*
r=randint(1,20)
spisok=[]
for i in range(r):
    spisok.append(randint(1,100))
print(spisok)
A=max(spisok)
print("самое большое",A)
L=len(spisok)
print("длина списка",L)
A2=(A/L)
print("ответ",A2)
ind=spisok.index(A)
spisok.insert(ind,A2)
print(spisok)
