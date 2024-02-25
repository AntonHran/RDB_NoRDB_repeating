from datetime import datetime

from faker import Faker


GROUPS_NUMBER: int = 3
STUDENTS_NUMBER: int = 50
TEACHERS_NUMBER: int = 6
SUBJECTS_NUMBER: int = 8
MIN_SUBJECTS_NUMBER: int = 2
MAX_SUBJECTS_NUMBER: int = 5
MIN_GRADE: int = 0
MAX_GRADE: int = 100
MIN_NUMBER_STUDENTS: int = 4
MAX_NUMBER_STUDENTS: int = 10
START_STUDY: datetime = datetime(year=2023, month=9, day=1)
FINISH_STUDY: datetime = datetime(year=2023, month=12, day=24)
WEEKEND: tuple = (5, 6)

fake = Faker("uk-UA")
