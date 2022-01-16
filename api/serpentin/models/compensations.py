from pony.orm import Required, Optional

from serpentin.core.database import db
from serpentin.models.statements import Statement


class Compensation(db.Entity):
    name = Required(str)
    type = Required(str)  # Can be Simple or Complex
    amount = Required(float)
    deals_count = Required(int)
    draft = Optional(bool)

    statement = Required(Statement)

    def get_formatted_data(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "amount": self.amount,
            "deals-count": self.deals_count,
            "draft": self.draft,
        }
