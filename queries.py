from sqlalchemy.orm import joinedload, subqueryload, outerjoin

from conf.db_connection import session
from conf.models import Teacher, Student, TeacherStudent


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
    teachers = session.query(Teacher).outerjoin(Teacher.students).all()
    # teachers = session.query(Teacher).options(joinedload(Teacher.students, innerjoin=True)).all()
    for t in teachers:
        columns = ["id", "fullname", "students"]
        result = [dict(zip(columns, (t.id, t.fullname, [(s.id, s.fullname) for s in t.students])))]
        print(result)


if __name__ == "__main__":
    # get_student_join()
    get_students()
    print()
    get_teachers()
