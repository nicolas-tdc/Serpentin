from pony.orm import Required, Set, Optional

from serpentin.core.database import db
from serpentin.helpers.sales import SalesHelpers


class Sales(db.Entity):
    name = Required(str)
    target = Optional(float)
    deals = Set("Deal")
    statements = Set("Statement")

    def get_sales(self) -> dict:
        """
        Returns formatted sales data with current month statement.
        :return:
        """
        sales_helpers = SalesHelpers()
        return {
            "id": self.id,
            "name": self.name,
            "target": self.target,
            "current_month_statement": sales_helpers.get_sales_monthly_statement(statements=self.statements, partial=True),
        }

    def get_sales_last_statements(self, count=12) -> dict:
        """
        Returns formatted sales data with n last statements (defaults to 12)
        :param count:
        :return: dict
        """
        sales_helpers = SalesHelpers()
        return {
            "id": self.id,
            "name": self.name,
            "target": self.target,
            "last_statements": sales_helpers.get_sales_last_statements(statements=self.statements, count=count),
        }

    def get_sales_deals(self) -> dict:
        """
        Returns formatted sales data with deals.
        :return:
        """
        sales_helpers = SalesHelpers()
        return {
            "id": self.id,
            "name": self.name,
            "target": self.target,
            "deals": sales_helpers.get_sales_deals(self.deals),
        }
