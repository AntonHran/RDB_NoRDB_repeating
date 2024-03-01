import datetime
import os
import sys

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade, Base
from read import return_model
from update import get_data, search_atr


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
    subject = session.query(Subject).filter_by(id=sub_id).first()
    return True if subject else False


def create_record(new_record):
    try:
        session.add(new_record)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)
    finally:
        session.close()


def fill_data(data: dict, table: Base, new_rec: Base) -> Base:
    for key in data.keys():
        field_to_fill = search_atr(table, key)
        if field_to_fill:
            print(field_to_fill)
            try:
                val = analyze_attrs(table, key, data.get(key))
                setattr(new_rec, field_to_fill, val)
            except (TypeError, ) as err:
                raise err
    return new_rec


def analyze_attrs(table: Base, key: str, val: str | int):
    if key.endswith("_id"):
        print(key)
        if search(table, val):
            return val
    if key.endswith("_date") or key == "date":
        return parse_data(val)
    return val


def search(table: Base, val: int):
    subject = session.query(table).filter_by(id=val).first()
    return True if subject else False


def parse_data(str_date: str) -> datetime.date:
    date_ = ""  # = datetime.date.today()
    try:
        year, month, day = str_date.split("-")
        date_ = datetime.date(year=int(year), month=int(month), day=int(day))
        return date_
    except TypeError as err:
        print(err)
    finally:
        return date_


def create_main(data: dict):
    data = get_data(data)
    table = return_model(data.get("model"))
    new_record = table()
    filled_rec = fill_data(data, table, new_record)
    create_record(filled_rec)
