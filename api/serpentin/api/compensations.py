from flask_restful import Resource
from serpentin.api import api
from serpentin.managers.compensations import get_compensations


class Compensations(Resource):
    def get(self):
        """Return compensations"""

        compensations = get_compensations()
        formatted_compensations = [compensation.get_formatted_data() for compensation in compensations]

        return {"compensations": formatted_compensations}


api.add_resource(Compensations, "/compensations")
