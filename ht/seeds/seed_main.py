from sqlalchemy.exc import SQLAlchemyError

from ht.config.db_connect import session
from ht.seeds.seed_groups import insert_groups
from ht.seeds.seed_students import insert_students
from ht.seeds.seed_teachers import insert_teachers
from ht.seeds.seed_subjects import insert_subjects
from ht.seeds.seed_grades import insert_grades


def insert_main():
    try:
        insert_groups()
        insert_students()
        insert_teachers()
        insert_subjects()
        insert_grades()
        session.commit()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    insert_main()
