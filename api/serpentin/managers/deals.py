from pony.orm import select

from serpentin.models.deals import Deal
from serpentin.models.sales import Sales


def get_deals() -> list[Deal]:
    return select(d for d in Deal)


def get_deals_by_sales(sales: Sales) -> list[Deal]:
    return sales.deals
