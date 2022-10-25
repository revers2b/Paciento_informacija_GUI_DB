from sqlalchemy.orm import sessionmaker
from paciento_info2 import engine, Pacientas, Kvepavimas, Kraujotaka, Neurologija

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Įvesti pacienta - 1 \nĮvesti kvepavima - 2 \nĮvesti kraujavima - 3 \nĮvesti neurologija - 4 \nPeržiūrėti paciento duomenys - 7 \nIšeit - 0:"))
    if pasirinkimas == 1:
            vardas = input("Įveskite varda: ")
            pavarde = input("Įveskite pavardė: ")
            asmens_kodas = int(input("Įveskite asmens koda: "))
            pacientas = Pacientas(vardas=vardas, pavarde=pavarde, asmens_kodas=asmens_kodas)
            session.add(pacientas)
            session.commit()
    if pasirinkimas == 2:
            spo2 = input("Įveskite SpO2: ")
            kd = input("Įveskite kvėpavimo dažni: ")
            priskirtas_pacientas_id = int(input("Įveskite paciento ID: "))
            kvepavimas = Kvepavimas(spo2=spo2, kd=kd, priskirtas_pacientas_id=priskirtas_pacientas_id)
            session.add(kvepavimas)
            session.commit()
    if pasirinkimas == 3:
            pulsas = input("Įveskite ŠSD: ")
            aks = input("Įveskite AKS: ")
            ekg = input("EKG: ")
            priskirtas_pacientas_id = int(input("Įveskite paciento ID: "))
            kraujo = Kraujotaka(pulsas=pulsas, aks=aks, ekg=ekg, priskirtas_pacientas_id=priskirtas_pacientas_id)
            session.add(kraujo)
            session.commit()
    if pasirinkimas == 4:
            gks = input("Įveskite GKS: ")
            gliukoze = input("Įveskite gliukozė: ")
            temp = input("Įveskite temp: ")
            priskirtas_pacientas_id = int(input("Įveskite paciento ID: "))
            neuro = Neurologija(gks=gks, gliukoze=gliukoze, temp=temp, priskirtas_pacientas_id=priskirtas_pacientas_id)
            session.add(neuro)
            session.commit()

    if pasirinkimas == 7:
        kvepuota = session.query(Kvepavimas).all()
        zmogus = session.query(Pacientas).all()
        kraujas = session.query(Kraujotaka).all()
        neuros = session.query(Neurologija).all()
        for zmones in zmogus:
            print(f"Vardas:{vardas}, Pavardė:{pavarde}, Asmens kodas:{asmens_kodas}")
        for deguonis in kvepuota:
            print(f"SpO2:{spo2}%, KD:{kd}")
        for krauja in kraujas:
            print(f"ŠSD:{pulsas}, AKS:{aks}, EKG:{ekg}")
        for madula in neuros:
            print(f"GKS:{gks}, Gliukozė:{gliukoze}, Temp:{temp}")
    if pasirinkimas == 0:
        break
    
