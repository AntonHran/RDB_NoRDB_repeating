from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("mobile_phone", String(25))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    students = relationship("Student",  # class to reference where to go to get
                            secondary="teachers_to_students",  # name of table m2m
                            back_populates="teachers")  # name of table to reference for students

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("mobile_phone", String(25))
    address = Column(String(100))
    teachers = relationship("Teacher",
                            secondary="teachers_to_students",
                            back_populates="students")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class TeacherStudent(Base):
    __tablename__ = "teachers_to_students"
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"))
