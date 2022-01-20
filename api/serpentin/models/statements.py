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
        return {
            "sales": self.sales.name,
            "month": self.month,
            "year": self.year,
            "deals_amount": self.deals_amount,
            "compensations": self.get_attached_compensations(),
        }

    def get_partial_data(self) -> dict:
        return {
            "deals_amount": self.deals_amount,
            "compensations": self.get_attached_compensations(),
        }

    def get_attached_compensations(self) -> dict:
        formatted_compensations = {}
        for compensation in self.compensations:
            if compensation.type == 'Simple':
                formatted_compensations['simple'] = compensation.get_partial_data()
            else:
                formatted_compensations['complex'] = compensation.get_partial_data()

        return formatted_compensations
