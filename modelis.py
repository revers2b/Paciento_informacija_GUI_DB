from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///informacija/pacientass.db')
Base = declarative_base()
session = sessionmaker(bind=engine)()
    
class Pacientas(Base):
    __tablename__ = "pacientas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asmens_kodas = Column("asmens kodas", Integer, unique=True)

class Kvepavimas(Base):
    __tablename__ = "kvepavimas"
    id = Column(Integer, primary_key=True)
    spo2 = Column("Spo2", Integer)
    kd = Column("kevpavimo daznis", Integer)
    pacientas_id = Column(Integer, ForeignKey("pacientas.id"))

class Kraujotaka(Base):
    __tablename__ = "kraujotaka"
    id = Column(Integer, primary_key=True)
    aks = Column("AKS", Integer)
    pulsas = Column("ŠSD", Integer)
    ekg = Column("EKG", Integer)

class Neurologija(Base):
    __tablename__ = "neurologija"
    id = Column(Integer, primary_key=True)
    gks = Column("GKS", Integer)
    gliukoze = Column("Gliukoze", Integer)
    temp = Column("Temperatura", Integer)

if __name__ == "__main__":
    Base.metadata.create_all(engine)