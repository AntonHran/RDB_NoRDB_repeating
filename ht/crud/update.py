import sys
import os
import re

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade, Base
from read import return_model


def update_row(record, table: Base, field: str, new_rec: str):
    try:
        record.update({getattr(table, field): new_rec})
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(err)


def get_data(arguments: dict) -> dict:
    return {key: value for key, value in arguments.items() if value}


def get_record(table: Base, id_: int):
    record = session.query(table).filter_by(id=id_)
    return record


def update_table(data: dict, record: Base, table_model: Base):
    for el in data.keys():
        field = search_atr(table_model, el)
        if field and field != "id":
            update_row(record, table_model, field, data.get(el))
            # record.update({getattr(table_model, field): data.get(el)})
    # session.commit()
    session.close()


def search_atr(table: Base, key: str) -> str:
    for atr in vars(table).keys():
        if re.match(atr, key):
            return atr


def update_main(data: dict):
    data = get_data(data)
    table_model = return_model(data.get("model"))
    record = get_record(table_model, data.get("id"))
    update_table(data, record, table_model)
