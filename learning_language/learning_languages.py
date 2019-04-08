import os
import random
import time


# Main

how_much_words=0
punkty=0
global grade

print("1. Angielski")
print("2. Niemiecki")
language=input("Wybor: ")
os.system("cls")

if int(language)==1:
    print("1. Cialo")
    print("2. Umiem")
    print("3. Mix")
    print("4. Czlowiek")
    print("5. Dom")
    print("6. Szkola")
    choice=input("Wybor: ")
    os.system("cls")
    if int(choice)==1:
        file="cialo.txt"
    elif int(choice)==2:
        file="umiem.txt"
    elif int(choice)==3:
        file="radek.txt"
    elif int(choice)==4:
        file="czlowiek.txt"
    elif int(choice)==5:
        file="dom.txt"
    elif int(choice)==6:
        file="szkola.txt"
elif int(language)==2:
    print("1. Cialo")
    print("2. Czasowniki")
    print("3. Kolory")
    print("4. Przedmioty szkolne")
    print("5. Przymiotniki")
    print("6. Rodzina")
    print("7. Rzeczowniki_mix")
    print("8. Zawody")
    choice=input("Wybor: ")
    os.system("cls")
    if int(choice)==1:
        file="cialo_n.txt"
    elif int(choice)==2:
        file="czasowniki_n.txt"
    elif int(choice)==3:
        file="kolory_n.txt"
    elif int(choice)==4:
        file="przedmioty_szkolne_n.txt"
    elif int(choice)==5:
        file="przymiotniki_n.txt"
    elif int(choice)==6:
        file="rodzina_n.txt"
    elif int(choice)==7:
        file="rzeczowniki_mix_n.txt"
    elif int(choice)==8:
        file="zawody_n.txt"

plik=open(str(file),"r")
dane=plik.readlines()

#print (a.readlines.__doc__)

if int(language)==1:
    print("1. Angielski->Polski")
    print("2. Polski->Angielski")
elif int(language)==2:
    print("1. Niemiecki->Polski")
    print("2. Polski->Niemiecki")
way_of_translating=input("Wybor: ")
os.system("cls")

print("1. Po kolei")
print("2. Losowo")
order=input("Wybor: ")
os.system("cls")

a=int(way_of_translating)-1
b=len(dane)-(3-int(way_of_translating))+2
bad_answers=[]
if int(order)==1:
    for i in range(a,b,2):
        print (dane[i])
        answer=input("Odpowiedz: ")
        if answer==dane[i+(3-2*int(way_of_translating))].strip():
            print("Dobrze")
            os.system("pause")
            punkty+=1
        else:
            if int(language)==2:
                tmp=dane[i+(3-2*int(way_of_translating))].strip()
                if tmp[4:]==answer:
                    print("Czesc jest dobrze wiec dam ci polowe punktow")
                    punkty+=0.5
                else:
                    print("Niestety zle!")
                    bad_answers.append(i)
            if int(language)==1:
                print("Niestety zle!")
                bad_answers.append(i)
            print("Poprawna odpowiedz: "+str(dane[i+(3-2*int(way_of_translating))].strip()))
            os.system("pause")
        os.system("cls")
elif int(order)==2:
    b-=2
    while 1:
        #lista=list(range(0,len(dane)-1))
        #random.shuffle(lista)
        random_value=random.randint(a,b-2)
        #random_value=lista[random_value]
        if random_value%2!=(int(way_of_translating)-1):
            random_value-=1
        print(dane[random_value])
        answer=input("Odpowiedz: ")
        if answer=="koniec":
            break
        elif answer==dane[random_value+(3-2*int(way_of_translating))].strip():
            print("Dobrze")
            os.system("pause")
            punkty+=1
        else:
            print("Niestety zle!")
            bad_answers.append(random_value)
            print("Poprawna odpowiedz: "+str(dane[random_value+(3-2*int(way_of_translating))].strip()))
            os.system("pause")
            os.system("cls")
            while 1:
                print("Powtarzasz!")
                print(dane[random_value])
                answer=input("Odpowiedz: ")
                if not answer: break
                elif answer==dane[random_value+(3-2*int(way_of_translating))].strip():
                    print("Teraz dobrze")
                    os.system("pause")
                    break
                else:
                    print("Znow zle!")
                    os.system("pause")
                    os.system("cls")
                    continue
        how_much_words+=1
        os.system("cls")
os.system("cls")
print("Koniec")
print("Zdobyles: "+str(punkty)+" punktow na ")
if int(order)==1:
    print(str(len(dane)/2))
    punkty=punkty*100.0/(len(dane)/2)
elif int(order)==2:
    print(how_much_words)
    punkty=punkty*100.0/how_much_words
if punkty<30:
    grade=1
elif punkty>=30 and punkty<50:
    grade=2
elif punkty>=50 and punkty<60:
    grade=3
elif punkty>=60 and punkty<70:
    grade=3.5
elif punkty>=70 and punkty<80:
    grade=4
elif punkty>=80 and punkty<90:
    grade=4.5
elif punkty>=90:
    grade=5
print("Procenty: "+str(round(punkty,2))+"; Ocena: "+str(grade))
jump=3-2*int(way_of_translating)
counter=1
print("\nPopelnione bledy: \n")
print("%-3s %-30s %-30s" % ("L.P","Slowo","Tlumaczenie"))
for i in bad_answers:
    print("%-3i %-30s %-30s" % (counter,dane[i].strip(),dane[i+jump].strip()))
    counter+=1
plik.close()
