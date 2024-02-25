from random import randint

from ht.config.models_ import Student
from ht.config.db_connect import session
from ht.seeds.initial_const import STUDENTS_NUMBER, GROUPS_NUMBER, fake


def insert_students():
    for _ in range(STUDENTS_NUMBER):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            group_id=randint(1, GROUPS_NUMBER)
        )
        session.add(student)
