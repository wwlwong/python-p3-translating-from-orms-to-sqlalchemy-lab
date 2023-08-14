from models import Dog
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    #session.add()
    session.commit()

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name.like(name)).all()

    for record in query:
        return record

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id.like(id)).all()

    for record in query:
        return record

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name.like(name), Dog.breed.like(breed)).all()

    for record in query:
        return record

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()