# -*- coding: utf-8 -*-

from configparser import ConfigParser
from imio.dataexchange.db import DBSession
from imio.dataexchange.db import DeclarativeBase
from imio.dataexchange.db.mappers.file import File
from imio.dataexchange.db.mappers.request import Request
from imio.dataexchange.db.mappers.router import Router
from sqlalchemy import engine_from_config
from sqlalchemy import text

import argparse
import os

File, Request, Router  # Pyflakes fix


def main():
    parser = argparse.ArgumentParser(description=u"Initialize the database")
    parser.add_argument('config_uri', type=str)

    args = parser.parse_args()
    config = ConfigParser()
    config.read(args.config_uri)

    engine = engine_from_config(config._sections.get('app:main'),
                                prefix='sqlalchemy.')
    DBSession.configure(bind=engine)
    DeclarativeBase.metadata.create_all(engine)

    import_data(DBSession)


def import_data(session):
    sql_file = open(os.path.join(os.path.dirname(__file__), 'db.sql'), 'r')
    session.execute(text(sql_file.read()))
    sql_file.close()
    session.commit()
