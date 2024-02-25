from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import joinedload, subqueryload, outerjoin

from conf.db_connection import session
from conf.models import Teacher, Student, Contact, TeacherStudent


def get_student_join():
    students = session.query(Student).join(Student.teachers).all()
    for s in students:
        columns = ["id", "fullname", "teachers"]
        result = [dict(zip(columns, (s.id, s.fullname, [(t.id, t.fullname) for t in s.teachers])))]
        print(result)


def get_students():
    # students = session.query(Student).options(joinedload(Student.teachers)).all()
    students = session.query(Student).options(subqueryload(Student.teachers)).limit(5).all()
    for s in students:
        columns = ["id", "fullname", "teachers"]
        result = [dict(zip(columns, (s.id, s.fullname, [(t.id, t.fullname) for t in s.teachers])))]
        print(result)


def get_teachers():
    teachers = session.query(Teacher).options(outerjoin(Teacher, Student)).all()  # ????????
    # teachers = session.query(Teacher).options(joinedload(Teacher.students, innerjoin=True)).all()
    for t in teachers:
        columns = ["id", "fullname", "students"]
        result = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.students])))]
        print(result)


def get_teachers_by_date():
    teachers = session.query(Teacher).options(joinedload(Teacher.students, innerjoin=True))\
        .filter(and_(Teacher.start_work >= (datetime(year=2020, month=1, day=1)),
                     Teacher.start_work <= (datetime(year=2021, month=12, day=31)))).all()
    for t in teachers:
        columns = ["id", "fullname", "start_work"]
        result = [dict(zip(columns, (t.id, t.fullname, t.start_work)))]
        print(result)


def get_student_with_contacts():
    students = session.query(Student).options(joinedload(Student.contacts)).all()
    for s in students:
        columns = ["id", "fullname", "contacts"]
        result = [dict(zip(columns, (s.id, s.fullname, [(c.id, c.fullname) for c in s.contacts])))]
        print(result)


def get_info():
    students = session.query(Student.id, Student.fullname, Teacher.fullname.label("teacher_fullname"),
                             Contact.fullname.label("contact_fullname")).select_from(Student)\
        .join(TeacherStudent).join(Teacher).join(Contact).all()
    for s in students:
        columns = ["id", "fullname", "teachers", "contacts"]
        result = [dict(zip(columns, (s.id, s.fullname, s.teacher_fullname, s.contact_fullname)))]
        print(result)


if __name__ == "__main__":
    # get_student_join()
    # get_students()
    # print()
    # get_teachers()
    # get_teachers_by_date()
    # get_student_with_contacts()
    get_info()
