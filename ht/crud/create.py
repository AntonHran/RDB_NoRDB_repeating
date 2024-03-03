import datetime
import os
import sys

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from config.models_ import Base
from read import return_model
from update import get_data, search_atr


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
            try:
                val = analyze_attrs(table, key, data.get(key))
                setattr(new_rec, field_to_fill, val)
            except (TypeError, ) as err:
                raise err
    return new_rec


def analyze_attrs(table: Base, key: str, val: str | int):
    if key.endswith("_id"):
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
