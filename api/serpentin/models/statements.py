from pony.orm import Required, Set, Optional

from serpentin.core.database import db
from serpentin.models.sales import Sales


class Statement(db.Entity):
    sales = Required(Sales)
    month = Required(int)
    year = Required(int)
    deals_amount = Optional(float)
    compensations = Set("Compensation")

    def get_formatted_data(self) -> dict:
        formatted_compensations = {}
        for c in self.compensations:
            # if c.draft is True:
            formatted_compensations['amount'] = c.amount
            formatted_compensations['type'] = c.type

        return {
            "sales": self.sales.name,
            "month": self.month,
            "year": self.year,
            "deals_amount": self.deals_amount,
            "compensation": formatted_compensations,
        }
