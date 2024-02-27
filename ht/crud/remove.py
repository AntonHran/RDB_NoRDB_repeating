import os
import sys

from sqlalchemy.exc import SQLAlchemyError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from config.db_connect import session
from crud.read import return_model


def remove_row(table: str, id_: int):
    table_model = return_model(table)
    if table_model:
        try:
            res = session.query(table_model).filter_by(id=id_).delete()
            session.commit()
            return res
        except SQLAlchemyError as err:
            print(err)
        finally:
            session.close()
    else:
        print("Check table name!")
