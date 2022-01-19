from pony.orm import select

from serpentin.models.statements import Statement
from serpentin.models.sales import Sales


def get_statements() -> list[Statement]:
    return select(statement for statement in Statement)


def get_statements_by_sales(sales: Sales) -> list[Statement]:
    return sales.statements
