from ht.config.db_connect import session
from ht.config.models_ import Group
from ht.seeds.initial_const import fake, GROUPS_NUMBER


def insert_groups():
    for _ in range(GROUPS_NUMBER):
        group = Group(name=fake.word())
        session.add(group)
