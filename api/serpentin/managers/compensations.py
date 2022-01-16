from pony.orm import select, db_session

from serpentin.models.compensations import Compensation


def get_simple_compensations() -> list[Compensation]:
    return select(c for c in Compensation if c.type == 'Simple')


def create_simple_compensation(name) -> Compensation:
    return Compensation(name=name, type='Simple')
