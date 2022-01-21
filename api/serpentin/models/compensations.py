from pony.orm import Required, Optional

from serpentin.core.database import db
from serpentin.models.statements import Statement


class Compensation(db.Entity):

    name = Required(str)
    type = Required(str)  # Can be Simple or Complex
    amount = Required(float)
    deals_count = Optional(int)
    closed_deals_count = Optional(int)
    draft = Optional(bool)

    statement = Required(Statement)

    def get_formatted_data(self) -> dict:
        """
        Returns full formatted compensation data.
        :return: dict
        """
        return {
            "name": self.name,
            "type": self.type,
            "amount": self.amount,
            "deals_count": self.deals_count,
            "closed_deals_count": self.closed_deals_count,
            "draft": self.draft,
        }

    def get_partial_data(self) -> dict:
        """
        Returns partial formatted compensation data.
        :return: dict
        """
        return {
            "amount": self.amount,
            "deals_count": self.deals_count,
            "closed_deals_count": self.closed_deals_count,
        }
