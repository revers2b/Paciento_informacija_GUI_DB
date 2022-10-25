from tkinter import *
# from modelis import Pacientas, Kvepavimas, Kraujotaka, Neurologija, session
from modelis import *
from sqlalchemy.orm import sessionmaker

window = Tk()
window.title("Paciento informacija")
session = sessionmaker(bind=engine)()


def saugoti():
    pacientas = Pacientas(vardas=vardas, pavarde=pavarde, asmens_kodas=asmens_kodas,)
    session.add(pacientas)
    session.commit()

def saugoti1():
    kvep = Kvepavimas(
        spo2=spo2,
        kd=kd,
    )
    session.add(kvep)
    session.commit()
def saugoti2():
    krau = Kraujotaka(
        aks=aks,
        pulsas=pulsas,
        ekg=ekg,
    )
    session.add(krau)
    session.commit()

def saugoti3():
    neur = Neurologija(
        gks=gks,
        gliukoze=gliukoze,
        temp=temp
    )
    session.add(neur)
    session.commit()

def isvalymas():
    vardas.delete(0, 'end')
    pavarde.delete(0, 'end')
    asmens_kodas.delete(0, 'end')
    spo2.delete(0, 'end')
    kd.delete(0, 'end')
    aks.delete(0, 'end')
    pulsas.delete(0, 'end')
    ekg.delete(0, 'end')
    gks.delete(0, 'end')
    gliukoze.delete(0, 'end')
    temp.delete(0, 'end')

# "({skaicius})" priklauso kodo gabalui kurie kartu siejasi
# (1) paciento informacija
pacientas_lab = Label(window, text="-Paciento informacija-", borderwidth=15, font="helvetica 15 bold")
vardas_lab = Label(window, text="Vardas:", anchor="e", font="helvetica 12")
vardas = Entry(window, width=50, font="helvetica 12")
pavarde_lab = Label(window, text="Pavarde:", anchor="e", font="helvetica 12")
pavarde = Entry(window, width=50, font="helvetica 12")
# amzius_lab = Label(window, text="Amzius:", anchor="e", font="helvetica 12")
# amzius = Entry(window, width=50, font="helvetica 12")
asmens_kodas_lab = Label(window, text="Asmens kodas:", anchor="e", font="helvetica 12")
asmens_kodas = Entry(window, width=50, font="helvetica 12")

# (2) paciento bukle
bukle = Label(window, text="-Bukle-", borderwidth=15, font="helvetica 15 bold")

# ------ A,B (kvepavimo takai, kvepavimas)
spo2_lab = Label(window, text="SpO2:", font="helvetica 12")
spo2 = Entry(window, width=2, font="helvetica 12")
kd_lab = Label(window, text="KD:", anchor="e", font="helvetica 12")
kd = Entry(window, width=2, font="helvetica 12")

# ------ C (kraujotaka)
aks_lab = Label(window, text="AKS:", anchor="e", font="helvetica 12")
aks = Entry(window, width=7, font="helvetica 12")
pulsas_lab = Label(window, text="ŠSD:", anchor="e", font="helvetica 12")
pulsas = Entry(window, width=3, font="helvetica 12")
ekg_lab = Label(window, text="EKG:", anchor="e", font="helvetica 12")
ekg = Entry(window, width=40, font="helvetica 12")

# ------ D (neurologija)
gks_lab = Label(window, text="GKS:", anchor="e", font="helvetica 12")
gks = Entry(window, width=2, font="helvetica 12")
gliukoze_lab = Label(window, text="Gliukoze:", anchor="e", font="helvetica 12")
gliukoze = Entry(window, width=5, font="helvetica 12")
temp_lab = Label(window, text="Temp:", anchor="e", font="helvetica 12")
temp = Entry(window, width=5, font="helvetica 12")

# (3) paciento atvykimo priezastis --- atideta del laiko---
# atvykimo_priezastis_lab = Label(window, text="-Atvykimo priezastis-", borderwidth=15, font="helvetica 15 bold", anchor="e")
# atvykimo_priezastis = Text(window, height=6, width=50, font="helvetica 12")

# (4) paciento vaistu paskirimas --- atideta del laiko---
# vaistai_pazymejimas_lab = Label(window, text="-Vaistai-", borderwidth=15, font="helvetica 15 bold")
# vaistai_laikas_lab = Label(window, text="Paskirimo laikas:", font="helvetica 12")
# vaistai_laikas = Entry(window, font="helvetica 12")
# vaistai_lab = Label(window, text="Vaistas:", font="helvetica 12")
# vaistai = Text(window, height=1, width=30, font="helvetica 12")
# vaistai_kiekis_lab = Label(window, text="Kiekis:", font="helvetica 12")
# vaistai_kiekis = Entry(window, font="helvetica 12")
# bukle_po_vaistu_geriau = Checkbutton(window, text="Geriau", font="helvetica 12")
# bukle_po_vaistu_nepakito = Checkbutton(window, text="Nepakito", font="helvetica 12")
# bukle_po_vaistu_blogiau = Checkbutton(window, text="Blogiau", font="helvetica 12")

# (5) Buttons
saugoti_irasymus = Button(window, text="Išsaugoti paciento informacija", height=2, width=15, font="helvetica 15", command=saugoti)
saugoti1_irasymus =Button(window, text="Išsaugoti kvepavimo informacija", height=2, width=15, font="helvetica 15", command=saugoti1)
saugoti2_irasymus =Button(window, text="Išsaugoti kraujotakos informacija", height=2, width=15, font="helvetica 15", command=saugoti2)
saugoti3_irasymus = Button(window, text="Išsaugoti neurologijos informacija", height=2, width=15, font="helvetica 15", command=saugoti3)


isvalyti_irasymus = Button(window, text="Išvalyti įrašymus", height=2, width=15, font="helvetica 15", command=isvalymas)
pacientu_sarasas = Button(window, text="pacientu sarasas", height=2, width=15, font="helvetica 15")

# (1) grid
pacientas_lab.grid(row=0, column=1)
vardas_lab.grid(row=1, column=0, sticky="e")
vardas.grid(row=1, column=1)
pavarde_lab.grid(row=2, column=0, sticky="e")
pavarde.grid(row=2, column=1)
# amzius_lab.grid(row=3, column=0, sticky="e")
# amzius.grid(row=3, column=1)
asmens_kodas_lab.grid(row=4, column=0, sticky="e")
asmens_kodas.grid(row=4, column=1)

# (2) grid
bukle.grid(row=6, column=1)
spo2_lab.grid(row=7, column=0, sticky="e")
spo2.grid(row=7, column=1, sticky="w")
kd_lab.grid(row=8, column=0, sticky="e")
kd.grid(row=8, column=1, sticky="w")
aks_lab.grid(row=9, column=0, sticky="e")
aks.grid(row=9, column=1, sticky="w")
pulsas_lab.grid(row=10, column=0, sticky="e")
pulsas.grid(row=10, column=1, sticky="w")
ekg_lab.grid(row=11, column=0, sticky="e")
ekg.grid(row=11, column=1, sticky="w")
gks_lab.grid(row=12, column=0, sticky="e")
gks.grid(row=12, column=1, sticky="w")
gliukoze_lab.grid(row=13, column=0, sticky="e")
gliukoze.grid(row=13, column=1, sticky="w")
temp_lab.grid(row=14, column=0, sticky="e")
temp.grid(row=14, column=1, sticky="w")

# (3) grid. ---atideta del laiko---
# atvykimo_priezastis_lab.grid(row=15, column=1, sticky="e")
# atvykimo_priezastis.grid(row=16, column=1, columnspan=2)

# (4) grid. ---atideta del laiko---
# vaistai_pazymejimas_lab.grid(row=17, column=0)
# vaistai_laikas_lab.grid(row=18, column=0, sticky="e")
# vaistai_laikas.grid(row=18, column=1, sticky="w")
# vaistai_lab.grid(row=18, column=2, sticky="e")
# vaistai.grid(row=18, column=3, sticky="w")
# vaistai_kiekis_lab.grid(row=18, column=4, sticky="e")
# vaistai_kiekis.grid(row=18, column=5, sticky="w")
# bukle_po_vaistu_geriau.grid(row=18, column=6)
# bukle_po_vaistu_nepakito.grid(row=18, column=7)
# bukle_po_vaistu_blogiau.grid(row=18, column=8)



#(5) grid
saugoti_irasymus.grid(row=1, column=3)
pacientu_sarasas.grid(row=2, column=3)
isvalyti_irasymus.grid(row=3, column=3)
saugoti1_irasymus.grid(row=1, column=4)
saugoti2_irasymus.grid(row=2, column=4)
saugoti3_irasymus.grid(row=3, column=4)

def close():
    window.destroy()

window.bind("<Escape>", lambda event: close())

window.mainloop()