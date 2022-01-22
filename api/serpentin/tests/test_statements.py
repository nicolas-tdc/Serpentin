import unittest
from pony.orm import db_session, select

from serpentin.app import create_app
from serpentin.core.database import connect_to_database
from serpentin.models.statements import Statement
from serpentin.models.sales import Sales
from serpentin.models.compensations import Compensation
from serpentin.managers.statements import get_statements


class StatementsTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("../tests/database.sqlite").test_client()
        self.db = connect_to_database("../tests/database.sqlite")

    @db_session
    def test_create_statements(self):
        sales = [
            Sales(name="First Sale"),
            Sales(name="Second Sale"),
        ]
        compensations = [
            Compensation(
                name="First Compensation",
                type="simple",
                amount=657
            ),
            Compensation(
                name="Second Compensation",
                type="complex",
                amount=1231,
            ),
        ]
        for i in range(2):
            Statement(
                sales=sales[i],
                month=2+i,
                year=2020+i,
                deals_amount=1375*(i+1),
                compensations=compensations[i],
            )

    @db_session
    def test_statements_api(self):
        test_statements = select(statement for statement in Statement)
        formatted_test_statements = []
        for statement in test_statements:
            formatted_test_statements.append(
                {
                    "sales": statement.sales.name,
                    "month": statement.month,
                    "year": statement.year,
                    "deals_amount": statement.deals_amount,
                    "compensations": statement.get_attached_compensations(),
                }
            )
        response = self.app.get('/api/statements')

        self.assertEqual(formatted_test_statements, response.json['statements'])
        self.assertEqual(200, response.status_code)

    @db_session
    def test_statements_managers(self):
        test_statements = select(statement for statement in Statement)
        formatted_test_statements = []
        for statement in test_statements:
            formatted_test_statements.append(
                {
                    "sales": statement.sales.name,
                    "month": statement.month,
                    "year": statement.year,
                    "deals_amount": statement.deals_amount,
                    "compensations": statement.get_attached_compensations(),
                }
            )
        statements = get_statements()
        formatted_statements = []
        for statement in statements:
            formatted_statements.append({
                "sales": statement.sales.name,
                "month": statement.month,
                "year": statement.year,
                "deals_amount": statement.deals_amount,
                "compensations": statement.get_attached_compensations(),
            })

        self.assertEqual(formatted_test_statements, formatted_statements)
