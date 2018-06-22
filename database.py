from mongoengine import connect

from models import Regeling, RegelingWaardes

connect('test')

def init_db():
    # Create the fixtures

    if 1 == 1:
        return

    print("******** inserted data *********")

    regelingwaardes = RegelingWaardes(
        franChise='10000.0',
        administratieKosten='0.01',
        WZPtoegestaan='true',
        PPtoegestaan='true',
        WZPpercentage='14.0',
        PPpercentage='70.0'
    )

    regeling = Regeling(
        regelingNummer=99,
        regelingNaam='Python generated',
        einddatum='2060-01-01',
        startDatum='2060-01-01',
        status='Actief',
        regelingWaardes=regelingwaardes
    )

    regeling2 = Regeling(
        regelingNummer=99,
        regelingNaam='Python generated numero 2',
        einddatum='2065-01-01',
        startDatum='2065-01-01',
        status='Actief',
        regelingWaardes=regelingwaardes
    )

    regeling.save()
    regeling2.save()
