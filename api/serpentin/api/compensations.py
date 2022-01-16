from flask_restful import Resource
from serpentin.api import api
from serpentin.managers.compensations import get_simple_compensations


class SimpleCompensations(Resource):
    def get(self):
        """Return simple compensations"""

        compensations = get_simple_compensations()
        formatted_compensations = [c.get_formatted_data() for c in compensations]

        return {"simple-compensations": formatted_compensations}


api.add_resource(SimpleCompensations, "/simple-compensations")
