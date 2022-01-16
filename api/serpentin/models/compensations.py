from pony.orm import Required, Set, Optional

from serpentin.core.database import db


class Compensation(db.Entity):
    name = Required(str)
    type = Required(str)  # Can be Simple or Complex
    draft = Optional(bool)

    statement_compensations = Set("StatementCompensation")

    def get_formatted_data(self) -> dict:
        return {"name": self.name}
