import sys
import os
import re

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade, Base
from read import return_model


def update_table(data: dict):
    data = get_data(data)
    search_field(data)


def get_data(arguments: dict):
    return {key: value for key, value in arguments.items() if value}


def search_field(data: dict):
    table_model = return_model(data.get("model"))
    record = session.query(table_model).filter_by(id=data.get("id"))
    for el in data.keys():
        field = search_atr(table_model, el)
        if field:
            record.update({getattr(record, field): data.get(el)})
    session.commit()
    session.close()


def search_atr(table: Base, key: str) -> str:
    for atr in vars(table).keys():
        if re.match(atr, key):
            return atr
