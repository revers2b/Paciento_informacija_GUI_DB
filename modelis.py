from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///informacija/pacientas.db')
Base = declarative_base()

class Pacientas(Base):
    __tablename__ = "pacientas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    amzius = Column("amzius", Integer)
    asmens_kodas = Column("asmens kodas", Integer, unique=True)
    atvykimo_data = Column("atvykimo data", Integer)

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.amzius}, {self.asmens_kodas}, {self.atvykimo_data})"

class Kvepavimas(Base):
    __tablename__ = "kvepavimas"
    id = Column(Integer, primary_key=True)
    spo2 = Column("Spo2", Integer)
    kd = Column("kevpavimo daznis", Integer)

    def __repr__(self):
        return f"{self.id}, {self.spo2}, {self.kd}"

class Kraujotaka(Base):
    __tablename__ = "kraujotaka"
    id = Column(Integer, primary_key=True)
    aks = Column("AKS", Integer)
    pulsas = Column("ŠSD", Integer)
    ekg = Column("Gliukoze", Integer)

    def __repr__(self):
        return f"{self.id}, {self.aks}, {self.pulsas}, {self.ekg}"

class Neurologija(Base):
    __tablename__ = "neurologija"
    id = Column(Integer, primary_key=True)
    gks = Column("GKS", Integer)
    gliukoze = Column("Gliukoze", Float)
    temperatura = Column("Temperatura", Float)

    def __repr__(self):
        return f"{self.id}, {self.gks}, {self.gliukoze}, {self.temperatura}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)