from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

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
    if otsitav_toit == StringVar():
        return None
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
            failist_toit = rida_listina[0].strip("\"").lower().capitalize()
            if võimalik_vaste in failist_toit:
                if abs(len(otsitav_toit) - len(failist_toit)) < 4:
                    failist_kaloraaž = leia_kaloraaž(rida_listina)
                    vasted[failist_toit] = failist_kaloraaž
                    return vasted
        fail.close()
        if vasted != {}:
            fail.close()
            return vasted

def vaste_listina(vasted):
    toidud = []
    for toit in vasted:
        toidud.append(toit)
    return toidud
    

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
                if i < 0:
                    raise Exception()
                print("Valitud toit on:", toidud[i])
                return toidud[i]
            except:
                print("Viga. Sisestage arv, mis on toote taga. Proovige uuesti.")
    elif otsus == "ei":
        veateade()
        uustoit()
        return None
    else:
        veateade()
        return None

def uustoit(toit, kalor):
    f = open("export.csv","a")
    f.write("\n"+'"'+uustoit+'"'+","+str(uuskalor))
    print("Toit lisatud andmebaasi.")
    f.close()

def andmete_sisestamine(sisend1, sisend2):
    toit = sisend1.capitalize()
    try:
        kogus = round(float(sisend2), 2)
    except:
        showinfo("Teade", "Sisend on vigane. Kontrollige, et kaloraaži lahtrisse on sisestatud ainult arv.")
        return
    tekst = "Kas sisestan faili järgmise kirje: \n" + str(toit) + "\n" + str(kogus) + " kcal saja grammi kohta"
    vastus = askyesno("Kinnitus", tekst)
    if vastus == "yes":
        uustoit(toit, kalor)
        showinfo("Teade", "Andmebaasi on täiendatud.")
    else:
        showinfo("Teade", "Toitu ei sisestatud.")


root = Tk()

#Akna nimi ja suurus
root.title("Kalori luger")
root.geometry("290x180")
#Akna erinevad tab'id ehk leheküljed
leheküljed = ttk.Notebook(root)
lehekülg1 = ttk.Frame(leheküljed)
lehekülg2 = ttk.Frame(leheküljed)
leheküljed.add(lehekülg1, text="Kalkulaator")
leheküljed.add(lehekülg2, text="Lisa toit")
leheküljed.pack(expand=1, fill="both")
    
#!!! ESIMENE LEHT !!!
#Raamid
raam_lahtrid = Frame(lehekülg1)
raam_nupp = Frame(lehekülg1)
raam_lahtrid.pack(side=TOP, pady=(30, 10))
raam_nupp.pack(side=TOP)
#Sildid
silt1 = Label(raam_lahtrid, text="Toiduaine: ")
silt2 = Label(raam_lahtrid, text="Kogus (g): ")
silt1.grid(row=3, column=0, pady=1, sticky=E)
silt2.grid(row=4, column=0, pady=1, sticky=E)
#Teksti alad
global sisend
sisend = StringVar()
toit = ttk.Combobox(raam_lahtrid, textvariable=sisend, width=17, height=10)

if sisend.get() != "":
    toit["values"] = vaste_listina(otsing(sisend.get()))
toit.grid(row=3, column=1)
kogus = Entry(raam_lahtrid)
kogus.grid(row=4, column=1)
#Nupud
sisesta_nupp = Button(raam_nupp, text="Enter",
                          command=lambda: andmete_sisestamine(toit.get(), kogus.get()))
sisesta_nupp.grid(row=6, column=3, pady=5, sticky="W")

#!!! TEINE LEHT !!!
#Raamid
raam_uustoit = Frame(lehekülg2)
raam_uuskaloraaž = Frame(lehekülg2)
raam_nupp = Frame(lehekülg2)
raam_uustoit.pack(side=TOP, pady=(10,10))
raam_uuskaloraaž.pack(side=TOP, pady=(0, 10))
raam_nupp.pack(side=TOP, pady=(5, 10))
#Uus toiduaine
uus_toit = StringVar()
silt1 = Label(raam_uustoit, text="Uus toiduaine: ")
silt1.pack(side=TOP)
toidu_nimi = Entry(raam_uustoit, textvariable=uus_toit)
toidu_nimi.pack(side=TOP)
#Kaloraaž
kaloraaž = StringVar()
silt2 = Label(raam_uuskaloraaž, text="Kaloraaž (100g kohta): ")
silt2.pack(side=TOP)
kogus = Entry(raam_uuskaloraaž, textvariable=kaloraaž)
kogus.pack(side=TOP)
#Nupp
uus_toit_nupp = Button(raam_nupp, text="Sisesta", command=lambda: andmete_sisestamine(uus_toit.get(), kaloraaž.get()))
uus_toit_nupp.grid(row=5, column= 1, sticky=W)
  
root.mainloop()
