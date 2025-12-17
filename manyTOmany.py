import sqlalchemy 
from sqlalchemy import create_engine,ForeignKey,Table
from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column,String,Integer,Float

engine=create_engine("sqlite:///student_courses.db",echo=True)
Base=declarative_base()

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)


class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    
    courses=relationship("Course",secondary=student_course,back_populates="students")
    
    

class Course(Base):
    __tablename__="courses"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    
    
    students=relationship("Student",secondary=student_course ,back_populates="courses")


Base.metadata.create_all(engine)

s1=Student(name="Prajwal")
s2=Student(name="Utsav")

c1=Course(title="Maths")
c2=Course(title="Physics")


s1.courses.append(c1)
s1.courses.append(c2)

s2.courses.append(c1)

from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)
session=Session()

session.add_all([s1,s2,c1,c2])
session.commit()


# reading data
# prints all the courses in which Prajwal has enrolled.
student=session.query(Student).filter_by(name="Prajwal").first()
for course in student.courses:
    print(course.title)


#prints all the students who are enrolled in physics
course=session.query(Course).filter_by(title="Physics").first()
for student in course.students:
    print(student.name)
    
# remove : breaks the relationship : student no longer take the course
# row remove from the student_course, student still exists, course still exists.
student1=session.query(Student).filter_by(name="Prajwal").first()
course1=session.query(Course).filter_by(title="Maths").first()
student1.courses.remove(course1)
session.commit()

# delete a student
student1=session.query(Student).filter_by(name="Prajwal").first()
session.delete(student1)
session.commit()

# delte a course 
course1=session.query(Course).filter_by(title="Maths").first()
session.delete(course1)
session.commit()