from pony.orm import Required, Set

from serpentin.core.database import db
from serpentin.models.compensations import Compensation
from serpentin.models.sales import Sales


class Statement(db.Entity):
    sales = Required(Sales)
    month = Required(int)
    year = Required(int)

    compensations = Set("StatementCompensation")

    def get_formatted_data(self) -> dict:
        return {
            "sales": self.sales.name,
            "month": self.month,
            "year": self.year,
        }


class StatementCompensation(db.Entity):
    compensation = Required(Compensation)
    statement = Required(Statement)
    amount = Required(float)

    def get_formatted_data(self) -> dict:
        return {
            "compensation": self.compensation.get_formatted_data(),
            "amount": self.amount,
        }
