from sqlalchemy.exc import SQLAlchemyError

from ht.config.db_connect import session
from ht.crud.read import return_model


def remove(table: str, id_: int):
    table_model = return_model(table)
    if table_model:
        try:
            session.delete(table_model).filter_by(id=id_).first()
            session.commit()
            return True
        except SQLAlchemyError as err:
            print(err)
        finally:
            session.close()
    else:
        print("Check table name!")
