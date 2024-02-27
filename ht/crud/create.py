import datetime
import os
import sys

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade


def create_group(gr_name: str):
    try:
        group = Group(name=gr_name)
        session.add(group)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()


def create_student(first_name: str, last_name: str, group_id: int):
    try:
        student = Student(
            first_name=first_name,
            last_name=last_name,
            group_id=group_id
        )
        session.add(student)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()


def create_subject(subj: str):
    try:
        subject = Subject(name=subj)
        session.add(subject)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()


def create_lector(first_name: str, last_name: str, start_date: str):
    try:
        lector = Teacher(
            first_name=first_name,
            last_name=last_name,
            start_work=parse_data(start_date)
        )
        session.add(lector)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()


def parse_data(str_date: str) -> datetime.date:
    date_ = ""  # = datetime.date.today()
    try:
        year, month, day = str_date.split("-")
        date_ = datetime.date(year=year, month=month, day=day)
        return date_
    except TypeError as err:
        print(err)
    finally:
        return date_


def create_grade(st_id: int, sub_id: int, grade: int, date: str):
    if check_stud_id(st_id) and check_subject_id(sub_id):
        try:
            grade = Grade(
                student_id=st_id,
                subject_id=sub_id,
                grade=grade,
                date=parse_data(date)
            )
            session.add(grade)
            session.commit()
        except SQLAlchemyError as err:
            session.rollback()
            print(err)
        finally:
            session.close()


def check_stud_id(st_id: int) -> bool:
    student = session.query(Student).filter_by(id=st_id).first()
    return True if student else False


def check_subject_id(sub_id: int) -> bool:
    student = session.query(Subject).filter_by(id=sub_id).first()
    return True if student else False
