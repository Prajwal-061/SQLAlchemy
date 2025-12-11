import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import String, Integer,Float,Column

engine= create_engine("sqlite:///day_1.db",echo=True)
Base=declarative_base()

class Employee(Base):
    __tablename__="employees"
    roll=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    cgpa=Column(Float)

class Course(Base):
    __tablename__="courses"
    course_id=Column(String,primary_key=True)
    title=Column(String)
    credit=Column(Integer)
    
Base.metadata.create_all(engine)
    
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()
E1=Employee(
    roll=12,
    name="alex",
    age=20,
    cgpa=9.4
)
E2=Employee(
    roll=11,
    name="Papu",
    age=21,
    cgpa=9.5
)
E3=Employee(
    roll=13,
    name="carry",
    age=25,
    cgpa=8.5
)
session.merge(E1)
session.merge(E2)
session.merge(E3)
session.commit()

course1=Course(
    course_id="CS3001",
    title="HPC",
    credit=3
)
course2=Course(
    course_id="CS3002",
    title="SE",
    credit=4
)
session.merge(course1)
session.merge(course2)
session.commit()

#updating the records
employee_pappu=session.query(Employee).filter(Employee.roll==11).first()
#print(f"Filtered Employee:\n{employee.name}\n{employee.roll}\n{employee.age}\n{employee.cgpa}")
if employee_pappu: 
   employee_pappu.age=22
   employee_pappu.cgpa=8.9
   session.commit()
else:
    print("no record found with this roll")

emp_Alex=session.query(Employee).filter(Employee.roll==12).first()
if emp_Alex:
    emp_Alex.name="Alex Parket"
    session.commit()
else:
    print("No records found for this roll")
    
    
employees=session.query(Employee).all()
for emp in employees:
    print(emp.name,emp.roll,emp.age,emp.cgpa)


# deleting the rows
emp_carry=session.query(Employee).filter(Employee.roll==13).first()

if emp_carry:
   session.delete(emp_carry)
   session.commit()
else:
    print("No records found for this roll")


#advance querying
