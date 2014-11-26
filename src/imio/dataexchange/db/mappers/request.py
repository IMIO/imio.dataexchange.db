# -*- coding: utf-8 -*-

from imio.dataexchange.db import DeclarativeBase
from imio.dataexchange.db.base import MapperBase
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import func


class Request(DeclarativeBase, MapperBase):
    __tablename__ = u'request'

    uid = Column(u'uid', Text, primary_key=True, unique=True, nullable=False)

    date = Column(u'date', DateTime, nullable=False, server_default=func.now())

    expiration_date = Column(u'expiration_date', DateTime)

    expired = Column(u'expired', Boolean, nullable=False,
                     server_default='false')
