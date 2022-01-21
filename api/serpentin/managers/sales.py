from pony.orm import select

from serpentin.models.sales import Sales


def get_sales() -> list[Sales]:
    """
    Returns list of sales.
    :return: list
    """
    return select(sale for sale in Sales)


def get_sale(sale_id) -> Sales:
    """
    Returns specific sales object.
    :param sale_id:
    :return: Sales
    """
    return Sales[sale_id]
