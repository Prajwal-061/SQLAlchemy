import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer,Float

engine= create_engine("sqlite:///students.db",echo=True)
Base=declarative_base()

class Student(Base):
    __tablename__="students"
    roll=Column(String,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    cgpa=Column(Float)
    
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)
session =Session()

student1=Student(
    roll="23053732",
    name="Prajwal",
    age=20,
    cgpa=9.4
)
student2=Student(
    roll="23053487",
    name="Abhinav",
    age=20,
    cgpa=9.4
)
student3=Student(
    roll="23053488",
    name="Aayush",
    age=20,
    cgpa=9.3
)
student4=Student(
    roll="23053419",
    name="Aayush Adhikari",
    age=21,
    cgpa=9.2
)
student5=Student(
    roll="23053418",
    name="Aashish Bastola",
    age=23,
    cgpa=9.0
)
session.merge(student1)
session.merge(student2)
session.merge(student3)
session.merge(student4)
session.merge(student5)
session.commit()

students=session.query(Student).all()
print(students)