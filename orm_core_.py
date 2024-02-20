from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData, create_engine
from sqlalchemy.sql import select


metadata = MetaData()

engine = create_engine("sqlite:///:memory:", echo=True)

users = Table("users", metadata,
              Column("id", Integer, primary_key=True),
              Column("fullname", String), )

addresses = Table("addresses", metadata,
                  Column("id", Integer, primary_key=True),
                  Column("email", String),
                  Column("user_id", Integer, ForeignKey("users.id")), )

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        insert_user = users.insert().values(fullname="Jack Jones")
        print(insert_user)
        result = conn.execute(insert_user)
        jones_id = result.lastrowid
        print(jones_id)
        insert_user = users.insert().values(fullname="John Daw")
        print(insert_user)
        result = conn.execute(insert_user)
        daws_id = result.lastrowid
        print(daws_id)

        result = conn.execute(select(users))
        for row in result:
            print(row)

        insrt_address = addresses.insert().values(email="jones@email.com", user_id=jones_id)
        conn.execute(insrt_address)
        insrt_address = addresses.insert().values(email="daw@email.com", user_id=daws_id)
        conn.execute(insrt_address)

        result = conn.execute(select(addresses))
        for row in result:
            print(row)

        sql_select = select(addresses.c.email, users.c.fullname).join(users)
        result = conn.execute(sql_select)
        for row in result:
            print(row)
