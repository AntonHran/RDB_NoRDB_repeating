from sqlalchemy import Integer, String, ForeignKey, create_engine, select, and_, or_, not_, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, Mapped, mapped_column


engine = create_engine("sqlite:///:memory:", echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[str] = mapped_column(String(120))


class Address(Base):
    __tablename__ = "addresses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped[User] = relationship("User")


Base.metadata.create_all(engine)

if __name__ == '__main__':
    n_user = User(fullname="Jack Jones")
    session.add(n_user)
    n_address = Address(email="jones@email.com", user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname="James Smith")
    session.add(n_user)
    n_address = Address(email="smith@email.com", user=n_user)
    session.add(n_address)
    n_address = Address(email="james_dam@email.com", user=n_user)
    session.add(n_address)
    n_address = Address(email="james@email.com", user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname="Jack Keating")
    session.add(n_user)
    n_address = Address(email="keating@email.com", user=n_user)
    session.add(n_address)
    session.commit()

    n_user = User(fullname="Adam Smith")
    session.add(n_user)
    n_address = Address(email="adam@email.com", user=n_user)
    session.add(n_address)
    n_address = Address(email="adam_smith@email.com", user=n_user)
    session.add(n_address)
    session.commit()

    statement = select(User.id, User.fullname)
    for row in session.execute(statement):
        print(row)

    statement_addr = select(Address.id, Address.email, User.fullname).join(Address.user)
    print(session.execute(statement_addr))
    print(session.execute(statement_addr).scalar())
    print(session.execute(statement_addr).scalars())

    for row in session.execute(statement_addr):
        print(row)

    columns = ["id", "fullname"]
    result = [dict(zip(columns, (row.id, row.fullname))) for row in session.execute(statement)]
    print(result)

    statement = select(User).where(User.fullname == "James Smith")
    result = session.execute(statement).scalar_one_or_none()
    if result:
        print(result.fullname)

    statement = select(User).where(User.fullname.like("Jack%"))
    result = session.execute(statement).scalars()
    for row in result:
        print(row.fullname)

    statement = select(User).where(User.fullname.like("Jack%")).where(User.id == 3)  # AND
    result = session.execute(statement).scalars()
    for row in result:
        print(row.fullname)

    statement = select(User).where(and_(User.fullname.like("Jack%"), User.id == 3))  # AND
    result = session.execute(statement).scalars()
    for row in result:
        print(row.fullname)

    statement = select(User).where(or_(User.fullname.like("Jack%"), User.id == 3))  # OR
    result = session.execute(statement).scalars()
    for row in result:
        print(row.fullname)

    statement = select(User).order_by(User.fullname)
    columns = ["id", "fullname"]
    result = [dict(zip(columns, (row.User.id, row.User.fullname))) for row in session.execute(statement)]
    print(result)

    statement = select(User.fullname, func.count(Address.id)).join(Address).group_by(User.fullname)
    res = session.execute(statement).all()
    print(res)

