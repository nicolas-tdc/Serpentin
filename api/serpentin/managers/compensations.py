from pony.orm import select

from serpentin.models.compensations import Compensation


def get_simple_compensations() -> list[Compensation]:
    return select(c for c in Compensation if c.type == 'Simple')
