from random import randint
from datetime import timedelta

from ht.config.models_ import Grade
from ht.config.db_connect import session
from ht.seeds.initial_const import (START_STUDY, FINISH_STUDY, STUDENTS_NUMBER, MIN_SUBJECTS_NUMBER,
                                    MAX_SUBJECTS_NUMBER, MIN_NUMBER_STUDENTS, MAX_NUMBER_STUDENTS,
                                    MIN_GRADE, MAX_GRADE, SUBJECTS_NUMBER, WEEKEND)


def insert_grades():
    num_days = (FINISH_STUDY - START_STUDY).days
    for day in range(num_days):
        cur_day = START_STUDY + timedelta(days=day)
        if cur_day.weekday() not in WEEKEND:
            subjects_per_day = randint(MIN_SUBJECTS_NUMBER, MAX_SUBJECTS_NUMBER)
            for _ in range(subjects_per_day):
                subject_id = randint(1, SUBJECTS_NUMBER)
                students_number = randint(MIN_NUMBER_STUDENTS, MAX_NUMBER_STUDENTS)
                for _ in range(students_number):
                    grade = Grade(
                        subject_id=subject_id,
                        student_id=randint(1, STUDENTS_NUMBER),
                        grade=randint(MIN_GRADE, MAX_GRADE),
                        date=cur_day.date())
                    session.add(grade)
