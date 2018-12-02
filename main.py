from tkinter import *
from tkinter import ttk

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
    
def p(event):
    global funktsioon
    return funktsioon.get()
    
    
    
def main():
    root = Tk()
    #Määratud akna nimi ja suurus
    root.title("Kalori luger")
    root.geometry("200x200")
    #Rakenduse erinevad tab'id ehk leheküljed
    leheküljed = ttk.Notebook(root)
    lehekülg1 = ttk.Frame(leheküljed)
    lehekülg2 = ttk.Frame(leheküljed)
    leheküljed.add(lehekülg1, text="Kalkulaator")
    leheküljed.add(lehekülg2, text="Lisa toit")
    leheküljed.pack(expand=1, fill="both")
    #Esimene leht
    #Sildid
    pealkiri = Label(lehekülg1, text="KALKULAATOR")
    tühik = Label(lehekülg1, text="")
    silt1 = Label(lehekülg1, text="Toiduaine: ")
    silt2 = Label(lehekülg1, text="Kogus: ")

    tühik.grid(row=2, column=0)
    pealkiri.grid(row=1, column=1, columnspan=2, sticky="w")
    silt1.grid(row=3, column=0, pady=1, sticky=E)
    silt2.grid(row=4, column=0, pady=1, sticky=E)
    root.mainloop()

main()


