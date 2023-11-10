import os.path
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import crud
import models
import schemas

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db_session():
    db = SessionLocal()
    try:  ## probeerd de sessie aan te maken en door te geven als dat niet lukt vangt hij het op zodat de app niet crashed
        yield db
    finally:
        db.close()


# Endpoint to create a film
@app.post("/films/", response_model=schemas.FilmOut)
def create_film(film: schemas.FilmCreate, db: Session = Depends(get_db_session)):
    db_film = crud.create_film(db, film)
    if db_film is None:
        raise HTTPException(status_code=500, detail="Film creation failed")
    return db_film


# Endpoint to get all films
@app.get("/films/", response_model=schemas.FilmListOut)
def read_films(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    films = crud.get_films(db, skip=skip, limit=limit)
    if not films:
        raise HTTPException(status_code=404, detail="No films found")
    return {"films": films}


# Endpoint to delete all films
@app.delete("/films/")
def delete_films(db: Session = Depends(get_db_session)):
    result = crud.delete_films(db)
    if result:
        raise HTTPException(status_code=500, detail="Failed to delete films")
    return {"message": "All films deleted"}


# Endpoint to create a person
@app.post("/persons/", response_model=schemas.PersonOut)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db_session)):
    db_person = crud.create_person(db, person)
    if db_person is None:
        raise HTTPException(status_code=500, detail="Person creation failed")
    return db_person


# Endpoint to get all persons
@app.get("/persons/", response_model=schemas.PersonListOut)
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    persons = crud.get_persons(db, skip=skip, limit=limit)
    if not persons:
        raise HTTPException(status_code=404, detail="No persons found")
    return {"persons": persons}


# Endpoint to delete all persons
@app.delete("/persons/")
def delete_persons(db: Session = Depends(get_db_session)):
    result = crud.delete_persons(db)
    if result:
        raise HTTPException(status_code=500, detail="Failed to delete persons")
    return {"message": "All persons deleted"}


# Endpoint to create a starship
@app.post("/starships/", response_model=schemas.StarshipOut)
def create_starship(starship: schemas.StarshipCreate, db: Session = Depends(get_db_session)):
    db_starship = crud.create_starship(db, starship)
    if db_starship is None:
        raise HTTPException(status_code=500, detail="Starship creation failed")
    return db_starship


# Endpoint to get all starships
@app.get("/starships/", response_model=schemas.StarshipListOut)
def read_starships(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_session)):
    starships = crud.get_starships(db, skip=skip, limit=limit)
    if not starships:
        raise HTTPException(status_code=404, detail="No starships found")
    return {"starships": starships}


# Endpoint to delete all starships
@app.delete("/starships/")
def delete_starships(db: Session = Depends(get_db_session)):
    result = crud.delete_starships(db)
    if result:
        raise HTTPException(status_code=500, detail="Failed to delete starships")
    return {"message": "All starships deleted"}


if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
