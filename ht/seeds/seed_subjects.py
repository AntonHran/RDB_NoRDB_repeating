from random import randint

from ht.config.db_connect import session
from ht.config.models_ import Subject
from ht.seeds.initial_const import fake, SUBJECTS_NUMBER, TEACHERS_NUMBER


def insert_subjects():
    for _ in range(SUBJECTS_NUMBER):
        subject = Subject(name=fake.word(), teacher_id=randint(1, TEACHERS_NUMBER))
        session.add(subject)
