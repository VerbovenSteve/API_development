from sqlalchemy.orm import Session

from models import Film, Person, Starship
from schemas import FilmCreate, PersonCreate, StarshipCreate


# CRUD operations for films
def create_film(db: Session, film: FilmCreate):
    db_film = Film(**film.dict())
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film


def get_films(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Film).offset(skip).limit(limit).all()


def delete_films(db: Session):
    db.query(Film).delete()
    db.commit()


# CRUD operations for persons
def create_person(db: Session, person: PersonCreate):
    db_person = Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Person).offset(skip).limit(limit).all()


def delete_persons(db: Session):
    db.query(Person).delete()
    db.commit()


# CRUD operations for starships
def create_starship(db: Session, starship: StarshipCreate):
    db_starship = Starship(**starship.dict())
    db.add(db_starship)
    db.commit()
    db.refresh(db_starship)
    return db_starship


def get_starships(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Starship).offset(skip).limit(limit).all()


def delete_starships(db: Session):
    db.query(Starship).delete()
    db.commit()
