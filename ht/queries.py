from sqlalchemy import func, desc, select, and_

from ht.config.models_ import Group, Grade, Student, Teacher, Subject
from ht.config.db_connect import session


def select_01():
    result = session.query(Student.id, Student.full_name, func.round(func.avg(Grade.grade), 2).label("average_grade"))\
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc("average_grade")).limit(5).all()
    return result



print(select_02())
