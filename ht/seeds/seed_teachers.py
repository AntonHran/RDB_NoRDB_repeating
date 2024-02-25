from ht.config.models_ import Teacher
from ht.config.db_connect import session
from ht.seeds.initial_const import TEACHERS_NUMBER, fake


def insert_teachers():
    for _ in range(TEACHERS_NUMBER):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date="-5y")
        )
        session.add(teacher)
