from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from web.models import Base


__Session = None
__engine = None

def get_engine():
    global __engine
    if not __engine:
        __engine = create_engine('sqlite:///db.sqlite', echo=True)
    return __engine

def get_session():
    global __Session
    if not __Session:
        engine = get_engine()
        Session = sessionmaker(bind=engine)
    return Session()

def build_schema():
    engine = get_engine()
    Base.metadata.create_all(engine)
