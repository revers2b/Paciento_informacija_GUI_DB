from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///informacija/paciento_info.db')
Base = declarative_base()


class Pacientas(Base):
    __tablename__ = "pacientas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asmens_kodas = Column("asmens kodas", Integer, unique=True)

class Kvepavimas(Base):
    __tablename__ = "Kvepavimas"
    id = Column(Integer, primary_key=True)
    spo2 = Column("spo2", String)
    kd = Column("kd", String)
    priskirtas_pacientas_id = Column(Integer, ForeignKey('pacientas.id'))

    def __repr__(self):
        return f"{self.id}, {self.spo2}, {self.kd}, {self.priskirtas_pacientas_id}"
    

class Kraujotaka(Base):
    __tablename__ = "Kraujotaka"
    id = Column(Integer, primary_key=True)
    pulsas = Column("pulsas", Integer)
    aks = Column("aks", Integer)
    ekg = Column("ekg", String)
    priskirtas_pacientas_id = Column(Integer, ForeignKey('pacientas.id'))

    def __repr__(self):
        return f"{self.id}, {self.pulsas}, {self.aks}, {self.ekg}, {self.priskirtas_pacientas_id}"

class Neurologija(Base):
    __tablename__ = "Neurologija"
    id = Column(Integer, primary_key=True)
    gks = Column("gks", Integer)
    gliukoze = Column("gliukoze", Integer)
    temp = Column("temp", Integer)
    priskirtas_pacientas_id = Column(Integer, ForeignKey('pacientas.id'))

    def __repr__(self):
        return f"{self.id}, {self.gks}, {self.gliukoze}, {self.temp}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)