import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.models import Teacher, Student, TeacherStudent
from conf.db_connection import session


STUDENTS_NUMBER = 20
TEACHERS_NUMBER = 6

fake = Faker("uk-UA")


def insert_students():
    for _ in range(STUDENTS_NUMBER):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)


def insert_teachers():
    for _ in range(TEACHERS_NUMBER):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date="-5y")
        )
        session.add(teacher)


def insert_rel_m2m():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()
    for student in students:
        rel = TeacherStudent(teacher_id=random.choice(teachers).id, student_id=student.id)
        session.add(rel)


def insert_rel_m2m_():
    for i in range(STUDENTS_NUMBER):
        teacher_student = TeacherStudent(
            teacher_id=random.randint(1, TEACHERS_NUMBER),
            student_id=i + 1
        )
        session.add(teacher_student)


def main():
    try:
        insert_teachers()
        insert_students()
        insert_rel_m2m()
        session.commit()
    except SQLAlchemyError as error:
        print(error)
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    main()
