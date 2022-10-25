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
    amzius = Column("amzius", Integer)
    asmens_kodas = Column("asmens kodas", Integer, unique=True)
    # kvepa = relationship("Pacientas", back_populates='kvepavimas')
    # kraujo = relationship("Kraujotaka", back_populates="pacientas")
    # neuro= relationship("Neurologija", back_populates="pacientas")

    def __repr__(self):
        return f"{self.id}, {self.vardas}, {self.pavarde}, {self.amzius}, {self.asmens_kodas}"

class Kvepavimas(Base):
    __tablename__ = "kvepavimas"
    id = Column(Integer, primary_key=True)
    spo2 = Column("Spo2", Integer)
    kd = Column("kevpavimo daznis", Integer)
    # pacientas_id = Column(Integer, ForeignKey("pacientas.id"))
    # pacientas = relationship("Pacientas", back_populates="kvepa")
    def __repr__(self):
        return f"{self.id}, {self.spo2}, {self.kd}"

class Kraujotaka(Base):
    __tablename__ = "kraujotaka"
    id = Column(Integer, primary_key=True)
    aks = Column("AKS", Integer)
    pulsas = Column("ŠSD", Integer)
    ekg = Column("EKG", Integer)
    # pacientas_id = Column("pacientas_id", Integer, ForeignKey("pacientas.id"))
    # pacientas = relationship("Pacientas", back_populates="kraujo")

    def __repr__(self):
        return f"{self.id}, {self.aks}, {self.pulsas}, {self.ekg}"

class Neurologija(Base):
    __tablename__ = "neurologija"
    id = Column(Integer, primary_key=True)
    gks = Column("GKS", Integer)
    gliukoze = Column("Gliukoze", Integer)
    temp = Column("Temperatura", Integer)
    # pacientas_id = Column("pacientas_id", Integer, ForeignKey("pacientas.id"))
    # pacientas = relationship("Pacientas", back_populates="neuro")

    def __repr__(self):
        return f"{self.id}, {self.gks}, {self.gliukoze}, {self.temp}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)