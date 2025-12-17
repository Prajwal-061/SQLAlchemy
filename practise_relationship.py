import sqlalchemy 
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column,String,Integer,Float

engine=create_engine("sqlite:///doctor_patients.db",echo=True)
Base=declarative_base()

class Doctor(Base):
    __tablename__="doctors"
    name=Column(String)
    id=Column(Integer,primary_key=True)
    specialization=Column(String)
    
    patients=relationship("Patient",back_populates="doctor",cascade="all,delete")
    
    
    
class Patient(Base):
    __tablename__="patients"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    doctor_id=Column(Integer,ForeignKey("doctors.id"),nullable=False)
    
    doctor=relationship("Doctor",back_populates="patients")
    
Base.metadata.create_all(engine)

D1=Doctor(name="Nasana",specialization="Cardiologist")
D2=Doctor(name="Alex",specialization="Neurologist")
D3=Doctor(name="Carry",specialization="Dermatologist")

P1=Patient(name="Prajwal",age=20,doctor=D1)
P2=Patient(name="Utsav",age=20,doctor=D1)
P3=Patient(name="Sara",age=21,doctor=D2)
P4=Patient(name="Harry",age=24,doctor=D2)
P5=Patient(name="Raj",age=22,doctor=D3)
P6=Patient(name="Sejal",age=25,doctor=D3)

from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)
session=Session()

session.add_all([D1,D2,D3])
session.commit()
session.add_all([P1,P2,P3,P4,P5,P6])
session.commit()

patients_under_nasana=session.query(Doctor).filter_by(name="Nasana").first()
print("patients under Dr. Nasana")
for p in patients_under_nasana.patients:
    print(p.name,p.age)
    
# sara is treated by which doctor?
sara=session.query(Patient).filter_by(name="Sara").first()
print(sara.doctor.name)


# this will result in the integrity error since many patients are associatated with doctors
# doctors can't make their patients orphan. for that we have to delete both.
doc=session.query(Doctor).filter_by(name="Nasana").first()
session.delete(doc)
session.commit()