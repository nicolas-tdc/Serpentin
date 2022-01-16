from pony.orm import select

from serpentin.models.compensations import Compensation


def get_simple_compensations() -> list[Compensation]:
    return select(c for c in Compensation if c.type == 'Simple' and c.draft is False)


def create_simple_compensation(name, draft=False) -> Compensation:
    return Compensation(name=name, draft=draft, type='Simple')
