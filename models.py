from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField,
     StringField, IntField)


class RegelingWaardes(EmbeddedDocument):
    franChise = StringField()
    administratieKosten = StringField()
    WZPtoegestaan = StringField()
    PPtoegestaan = StringField()
    WZPpercentage = StringField()
    PPpercentage = StringField()


class Regeling(Document):
    meta = {'collection': 'regeling'}
    regelingNummer = IntField()
    regelingNaam = StringField()
    einddatum = DateTimeField(default=datetime.now)
    startDatum = DateTimeField(default=datetime.now)
    status = StringField()
    regelingWaardes = EmbeddedDocumentField(RegelingWaardes)
