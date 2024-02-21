from sqlalchemy import Integer, String, ForeignKey, create_engine, select
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
    session.commit()

    n_user = User(fullname="Jack Keating")
    session.add(n_user)
    n_address = Address(email="keating@email.com", user=n_user)
    session.add(n_address)
    session.commit()

    statement = select(User.id, User.fullname)
    for row in session.execute(statement):
        print(row)

    statement = select(Address.id, Address.email, User.fullname).join(Address.user)
    for row in session.execute(statement):
        print(row)

