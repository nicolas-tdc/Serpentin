from pony.orm import select

from serpentin.models.compensations import Compensation


def get_compensations() -> list[Compensation]:
    """
    Returns list of compensations.
    :return: list
    """
    return select(compensation for compensation in Compensation)
