import sqlalchemy
from sqlalchemy.orm import Session as SqlSession
from .common import SqlTableBase


class Storage:
    def __init__(self, db_url: str, **kwargs):
        engine = sqlalchemy.create_engine(url=db_url, **kwargs)
        SqlTableBase.metadata.create_all(engine)
        self.__session = SqlSession(engine)

    def save(self, objects):
        # List of objects
        if type(objects) == list:
            with self.__session.begin():
                for obj in objects:
                    obj.save(self.__session)
            return

        # One object
        objects.save(self.__session)

    def load(self, entity, primary_key):
        return self.__session.get(entity=entity, ident=primary_key)

    def load_all(self, entity):
        return self.__session.query(entity).all()
