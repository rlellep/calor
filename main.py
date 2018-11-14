from tkinter import *

def veateade():
    print("Teie toodet ei leitud... Proovige uuesti.")
    print("Soovitused:")
    print("1. Teie sisestatud toit oli liiga spetsiifiline. Proovige üldisemalt toitu kirja panna.")
    print("2. Teie sisestatud toiduaine polnud korrektselt kirja pandud. Veenduge, et sisestatud toidu nimetus on korrektne.")

def kaloraaži_leidmine(toit, toitude_kaloraaž):
    söödud_kogus = round(float(input("Sisesta kogus grammides: ")), 2)
    toidu_kaloraaž = toitude_kaloraaž[toit]/100
    return round(söödud_kogus * toidu_kaloraaž, 2)

def leia_kaloraaž(list):
    for kaloraaž in list:
        try:
            return float(kaloraaž)
        except(ValueError):
            continue
        
def otsing(otsitav_toit, faili_nimi="export.csv"):
    vasted = {}
    fail = open(faili_nimi)
    for rida in fail:
        rida_listina = rida.split(",")
        failist_toit = rida_listina[0].strip("\"")
        if otsitav_toit in failist_toit:
            failist_kaloraaž = leia_kaloraaž(rida_listina)
            vasted[failist_toit] = round(failist_kaloraaž,2)
    fail.close()
    return vasted

def süva_otsing(otsitav_toit, faili_nimi="export.csv"):
    vasted = {}
    for i in range(len(otsitav_toit), 0, -1):
        võimalik_vaste = otsitav_toit[:i]
        fail = open(faili_nimi)
        for rida in fail:
            rida_listina = rida.split(",")
            failist_toit = rida_listina[0].strip("\"").lower()
            if võimalik_vaste in failist_toit:
                if abs(len(otsitav_toit) - len(failist_toit)) < 4:
                    failist_kaloraaž = leia_kaloraaž(rida_listina)
                    vasted[failist_toit] = round(failist_kaloraaž,2)
        fail.close()
        if vasted != []:
            fail.close()
            return vasted

def valikute_töötlemine(valikud):
    print("Teie otsingule leiti järgmised vasted: ")
    toidud = []
    for toit in valikud:
        toidud += [toit]
    for indeks, toit in enumerate(toidud):
        print("(" +str(indeks+1)+ ")",toit)
    otsus = input("Kas nimekirjas leidub sinu toode(jah/ei): ")
    if otsus == "jah":
        while True:
            try:
                i = int(input("Sisestage vastav number:  "))-1
                print("Valitud toit on:", toidud[i])
                return toidud[i]
            except(IndexError):
                print("Viga. Sisestage arv, mis on toote taga. Proovige uuesti.")
    elif otsus == "ei":
        veateade()
        uustoit()
        return None
    else:
        veateade()
        return None

def uustoit():
    uus = input("3. Toit puudub andmebaasist. Soovite lisada andmebaasi uue toidu?(jah/ei): ")
    if uus == "jah":
        uustoit = input("Sisestage uue toidu nimi (sinna järele soovitatavalt ka kirjeldus): ").lower().capitalize()
        uuskalor = float(input("Sisestage toidu kaloraaz 100 grammi kohta: "))+0.0000001
        f = open("export.csv","a")
        f.write("\n"+'"'+uustoit+'"'+","+str(uuskalor))
        print("Toit lisatud andmebaasi.")
        f.close()
    else:
        return None
    
        
print("--------------------------------------")
print("---------KALORAAŽI KALKULAATOR--------")
print("--------------------------------------")

while True:
    print()
    toit = input("Sisesta toit: ").lower().capitalize()
    valikud = {}
    valikud.update(otsing(toit))
    valikud.update(süva_otsing(toit))
    if valikud != {}:
        tarbitud_toit = valikute_töötlemine(valikud)
    else:
        veateade()
        uustoit()
        tarbitud_toit = None
    if tarbitud_toit != None:
        kaloraaž = kaloraaži_leidmine(tarbitud_toit, valikud)
        print(kaloraaž, "kcal")
    #print()
    print("Väljumiseks sisesta q. Uue otsingu jaoks vajuta ENTER. ")
    käsklus = input("")
    if käsklus.lower() == "q":
        break
print("Nägemiseni!")
    
    
"""   
root = Tk() 
#Määratud akna suurus
root.geometry("400x250")
root.title("Kalori luger")
#Raamide loomine
#Teksti alad
juhis_toit = Label(root, text="Toiduaine:")
juhis_toit.grid(row=0, column=0)
toit = Entry(root)
toit.grid(row=0, column=1)
juhis_kogus = Label(root, text="Kogus:")
juhis_kogus.grid(row=1, column=0)
kogus = Entry(root)
kogus.grid(row=1, column=1)
#Listbox 
listbox = Listbox(root)
listbox.grid(row=1, column=2)
#Nupp
button = Button(text="Close")
button.grid(row=6, column=5)
#Vastused
toiduaine = "Vali toiduaine"
kogus = "0000"
valitud_toiduaine = Label(root, text=toiduaine)
#valitud_toiduaine.grid(row = 2, column=1)
kogus = Label(root, text=kogus)
#kogus.grid(row = 2, column=2)

root.mainloop()
"""


