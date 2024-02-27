import sys
import os

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Group, Student, Subject, Teacher, Grade


def update_table(data):
    ...
