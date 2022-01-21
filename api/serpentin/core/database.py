from pony.orm import Database

db = Database()


# Test database

db.bind(provider="sqlite", filename="../tests/database.sqlite", create_db=True)

from serpentin.models import compensations
from serpentin.models import deals
from serpentin.models import sales
from serpentin.models import statements

db.generate_mapping(create_tables=True)


# Provision database

def connect_to_database():
    db.provider = db.schema = None
    db.bind(provider="sqlite", filename="./database.sqlite", create_db=True)

    from serpentin.models import compensations
    from serpentin.models import deals
    from serpentin.models import sales
    from serpentin.models import statements

    db.generate_mapping(create_tables=True)
