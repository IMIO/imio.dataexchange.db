# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import register


DBSession = scoped_session(sessionmaker())
register(DBSession)

DeclarativeBase = declarative_base()


def temporary_session(engine):
    """Return a session that can be used without transaction manager"""
    return scoped_session(sessionmaker(bind=engine))
