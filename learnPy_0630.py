import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

Base = sqlalchemy.orm.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)


Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person = Person(name='Mike')
session.add(person)
person = Person(name='BBB')
session.add(person)
person = Person(name='CCC')
session.add(person)
session.commit()

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.commit()
p5 = session.query(Person).filter_by(name='BBB').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()

for person in persons:
    print(person.id, person.name)