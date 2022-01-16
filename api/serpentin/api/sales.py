from flask_restful import Resource
from serpentin.api import api
from serpentin.managers.sales import get_sales


class Sales(Resource):
    def get(self):
        """Return sales"""

        sales = get_sales()
        formatted_sales = [s.get_formatted_data() for s in sales]

        return {"sales": formatted_sales}


api.add_resource(Sales, "/sales")
