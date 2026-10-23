# -*- coding: utf-8 -*-

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


# Apps that want the transaction manager call zope.sqlalchemy.register(DBSession)
DBSession = scoped_session(sessionmaker())
DeclarativeBase = declarative_base()


def temporary_session(engine):
    """Return a session that can be used without transaction manager"""
    return scoped_session(sessionmaker(bind=engine))
