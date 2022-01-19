from pony.orm import select

from serpentin.models.deals import Deal
from serpentin.models.sales import Sales


def get_deals() -> list[Deal]:
    return select(deal for deal in Deal)
