from pprint import pprint
import os
import sys

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade


def read_table(table: str, id_: int):
    table_model = return_model(table)
    if table_model:
        try:
            res = session.query(table_model).filter_by(id=id_).first()
            return res
        except SQLAlchemyError as err:
            print(err)
        finally:
            session.close()
    else:
        print("Check table name!")


tables = {"Group": Group,
          "Student": Student,
          "Subject": Subject,
          "Teacher": Teacher,
          "Grade": Grade, }


def return_model(table_name: str):
    if table_name in tables.keys():
        return tables.get(table_name)
    return


def read_result(table: str, id_: int):
    res = read_table(table, id_)
    if res:
        pprint(res.__dict__)
    else:
        print("Nothing...")
