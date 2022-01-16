from pony.orm import Required, Set, Optional

from serpentin.core.database import db


class Sales(db.Entity):
    name = Required(str)
    target = Optional(float)
    deals = Set("Deal")
    statements = Set("Statement")

    def get_formatted_data(self) -> dict:
        return {
            "name": self.name,
            "target": self.target,
        }
