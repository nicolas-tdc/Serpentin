from pony.orm import select

from serpentin.models.deals import Deal


def get_deals() -> list[Deal]:
    """
    Returns list of deals.
    :return: list
    """
    return select(deal for deal in Deal)
