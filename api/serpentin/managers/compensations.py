from pony.orm import select

from serpentin.models.compensations import Compensation


def get_compensations() -> list[Compensation]:
    return select(compensation for compensation in Compensation)
