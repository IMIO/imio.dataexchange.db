# -*- coding: utf-8 -*-

from imio.dataexchange.db import DBSession
from sqlalchemy import and_
from sqlalchemy import exists


class MapperBase(object):

    @classmethod
    def _build_filter(cls, operator=and_, **kwargs):
        filters = []
        for key, value in kwargs.items():
            column = getattr(cls, key)
            filters.append(column == value)
        return operator(*filters)

    def insert(self, flush=False, commit=False):
        DBSession.add(self)
        if flush is True:
            DBSession.flush()
        if commit is True:
            DBSession.commit()

    update = insert

    def delete(self, flush=False, commit=False):
        DBSession.delete(self)
        if flush is True:
            DBSession.flush()
        if commit is True:
            DBSession.commit()

    @classmethod
    def exists(cls, **kwargs):
        return DBSession.query(exists().where(cls._build_filter(**kwargs))).scalar()

    @classmethod
    def first(cls, options=[], order_by=[], **kwargs):
        query = cls.query(options=options, order_by=order_by, **kwargs)
        return query.first()

    @classmethod
    def count(cls, options=[], **kwargs):
        query = cls.query(options=options, **kwargs)
        return query.count()

    @classmethod
    def get(cls, options=[], order_by=[], limit=None, **kwargs):
        query = cls.query(options=options, order_by=order_by, **kwargs)
        return query.all()

    @classmethod
    def query(cls, options=[], order_by=[], **kwargs):
        query = DBSession.query(cls)
        query = query.options(options)
        if order_by:
            if isinstance(order_by, list):
                query = query.order_by(*order_by)
            else:
                query = query.order_by(order_by)
        return query.filter(cls._build_filter(**kwargs))
