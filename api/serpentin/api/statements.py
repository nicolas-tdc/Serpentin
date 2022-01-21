from flask_restful import Resource

from serpentin.api import api
from serpentin.managers.statements import get_statements, get_statements_by_sales


class Statements(Resource):
    def get(self):
        """Return statements"""

        statements = get_statements()
        formatted_statements = [statement.get_formatted_data() for statement in statements]

        return {"statements": formatted_statements}


api.add_resource(Statements, "/statements")