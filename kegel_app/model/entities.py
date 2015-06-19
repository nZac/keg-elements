from __future__ import absolute_import, unicode_literals

from keg.db import db


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    color = db.Column(db.Unicode)
