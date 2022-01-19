from pony.orm import select

from serpentin.models.sales import Sales


def get_sales() -> list[Sales]:
    return select(sale for sale in Sales)


def get_sale(sale_id) -> Sales:
    return Sales[sale_id]
