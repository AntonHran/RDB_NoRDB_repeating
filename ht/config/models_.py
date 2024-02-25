from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(10))


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("mobile_phone", String(25))
    address = Column(String(100))
    group_id = Column(Integer, ForeignKey("groups.id", onupdate="CASCADE", ondelete="CASCADE"))
    grades = relationship("Student",  # class to reference where to go to get
                          secondary="grades",  # name of table m2m
                          back_populates="students")

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE"))


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(100))
    phone = Column("mobile_phone", String(25))
    address = Column(String(100))
    start_work = Column(Date, nullable=False)
    grades = relationship("Student",  # class to reference where to go to get
                          secondary="grades",  # name of table m2m
                          back_populates="teachers")  # name of table to reference for students

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE"))
    grade = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
