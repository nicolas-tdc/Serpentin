from flask_restful import Resource
from serpentin.api import api
from serpentin.managers.sales import get_sales, get_sale


class Sales(Resource):

    def get(self):
        """
        Returns formatted list of sales.
        :return: dict
        """

        sales = get_sales()
        formatted_sales = [sale.get_sales() for sale in sales]

        return {"sales": formatted_sales}


api.add_resource(Sales, "/sales")


class SingleSalesStatements(Resource):

    def get(self, sale_id):
        """
        Returns formatted list of statements for a specific sales
        :return: dict
        """
        sale = get_sale(sale_id)

        return {"sales": sale.get_sales_last_statements()}


api.add_resource(SingleSalesStatements, "/sales/<int:sale_id>/statements")


class SingleSalesDeals(Resource):

    def get(self, sale_id):
        """
        Returns formatted list of deals for a specific sales
        :return: dict
        """
        sale = get_sale(sale_id)

        return {"sales": sale.get_sales_deals()}


api.add_resource(SingleSalesDeals, "/sales/<int:sale_id>/deals")
