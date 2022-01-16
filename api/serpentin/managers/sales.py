from pony.orm import select

from serpentin.models.sales import Sales


def get_sales() -> list[Sales]:
    return select(s for s in Sales)
