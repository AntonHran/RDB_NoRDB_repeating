import sys
import os
import re

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade
from read import return_model


def update_table(data: dict):
    data = get_data(data)
    print(data)


def get_data(arguments: dict):
    return {key: value for key, value in arguments.items() if value}


def search_field(data: dict):
    table_model = return_model(data.get("model"))
    record = session.query(table_model).filter_by(id=data.get("id"))
    for el in data.keys():
        if getattr(table_model, el):
            record.update()