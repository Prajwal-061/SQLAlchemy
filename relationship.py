import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column,String,Integer,Float,ForeignKey

engine=create_engine("sqlite:///employee.db",echo=True)
Base=declarative_base()

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dept_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    department = relationship("Department", back_populates="employees")
 

Base.metadata.create_all(engine)

dept1=Department(id=23,name="CSE")
dept2=Department(id=24,name="IT")

emp1=Employee(id=11,name="Prajwal",department=dept1)
emp2=Employee(id=12,name="Abhinav",department=dept1)
emp3=Employee(id=13,name="Abhi",department=dept2)
emp4=Employee(id=14,name="Ayush",department=dept2)


from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()


session.merge(dept1)
session.merge(dept2)
session.merge(emp1)
session.merge(emp2)
session.merge(emp3)
session.merge(emp4)
session.commit()

cse=session.query(Department).filter_by(name="CSE").first()
for emp in cse.employees:
    print(emp.id, emp.name)
    
# which department does prajwal belong to?
emp= session.query(Employee).filter_by(name="Prajwal").first()
print(emp.department.name)
