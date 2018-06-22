from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, EmbeddedDocumentField, GenericEmbeddedDocumentField,
    ListField, ReferenceField, StringField, IntField,
    EmbeddedDocumentListField)

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
    einddatum = StringField()
    startDatum = StringField()
    status = StringField()
    regelingWaardes = EmbeddedDocumentField(RegelingWaardes)