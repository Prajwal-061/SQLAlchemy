import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import String, Integer,Float,Column
from sqlalchemy import desc

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
E4=Employee(
    roll=14,
    name="Harry",
    age=25,
    cgpa=8.57
)
E5=Employee(
    roll=15,
    name="Kajal",
    age=23,
    cgpa=8.0
)
session.merge(E1)
session.merge(E2)
session.merge(E3)
session.merge(E4)
session.merge(E5)
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
#employee age greater than 20
emp_20=session.query(Employee).filter(Employee.age > 20).all()
for e in emp_20:
    print(e.name,e.roll,e.age,e.cgpa,)
    

# employee name containing letter a
emp_a=session.query(Employee).filter(Employee.name.like("%a%")).all()
for emps in emp_a:
    print(emps.name)

#emp
print("Either roll 11 or 12\n")
emp_11_12=session.query(Employee).filter(Employee.roll.in_([11,12])).all()
for i in emp_11_12:
    print(i.name,i.age,i.cgpa,i.roll)

#order_by
emp_cgpa=session.query(Employee).order_by(desc(Employee.cgpa)).all()
for j in emp_cgpa:
    print(j.cgpa)
  
# count total employess  
total_employee=session.query(Employee).count()
print(total_employee)

# select specific column
emp_name=session.query(Employee.name).all()
for k in emp_name:
    print(k.name)