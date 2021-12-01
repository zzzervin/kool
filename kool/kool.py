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


                                    #not work

#from random import*
#spisok=spisok_=[]

#for i in range(6):
#    spisok.append(randint(-100,100))
#print(spisok)
#for n in spisok:
#    spisok_.append(abs(n))
#spisok_.sort()
#print(spisok_)
#spisok_.sort(reverse=True)
#print(spisok_)

                                    #######    


#L1=['крот', 'белка', 'выхухоль']
#L2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
#L3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
#SS=[L1,L2,L3]
#N=0
#while N<len(SS):
#    print(SS[N])
#   pikkem=0
#    sN_=[]
#    for s in SS[N]:
#        pikkus=len(s)
#        if pikkus>pikkem:pikkem=pikkus
#    for s in SS[N]:
#        sN_.append(s.ljust(pikkem,'*'))
#    print(sN_)
#    N+=1


                                    #Dlaj intrgrca
while 1:
    Maakonnad=["Tallin","Narva",]
    iseloom=[1000,2000]
    n=int(input())
    print(Maakonnad[n],iseloom[n])
