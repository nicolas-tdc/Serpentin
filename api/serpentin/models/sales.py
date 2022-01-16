from pony.orm import Required, Set

from serpentin.core.database import db


class Sales(db.Entity):
    name = Required(str)
    deals = Set("Deal")
    statements = Set("Statement")
