from pony.orm import select

from serpentin.models.statements import Statement


def get_statements() -> list[Statement]:
    """
    Returns list of statements.
    :return: list
    """
    return select(statement for statement in Statement)
