import unittest
import pytest
from pony.orm import db_session, select

from serpentin.app import create_app
from serpentin.core.database import connect_to_database
from serpentin.models.deals import Deal
from serpentin.managers.deals import get_deals


class DealsTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app("../tests/database.sqlite").test_client()
        self.db = connect_to_database("../tests/database.sqlite")

    @staticmethod
    def deals_test_data():
        return [
            {
                'name': 'First deal',
                'active': True,
                'modified': False,
                'amount': 950,
                'closed': False,
                'close_date': None,
                'owner': None
            },
            {
                'name': 'Second deal',
                'active': True,
                'modified': True,
                'amount': 1750,
                'closed': False,
                'close_date': None,
                'owner': None
            },
        ]

    @db_session
    def test_create_deals(self):
        for deal in self.deals_test_data():
            Deal(
                name=deal['name'],
                active=deal['active'],
                modified=deal['modified'],
                amount=deal['amount'],
                closed=deal['closed'],
                close_date=deal['close_date'],
                owner=deal['owner'],
            )

    @db_session
    def test_deals_api(self):
        response = self.app.get('/api/deals')

        self.assertEqual(self.deals_test_data(), response.json['deals'])
        self.assertEqual(200, response.status_code)

    @db_session
    def test_deals_managers(self):
        deals = get_deals()
        formatted_deals = []
        for deal in deals:
            formatted_deals.append({
                "name": deal.name,
                "active": deal.active,
                "modified": deal.modified,
                "amount": deal.amount,
                "closed": deal.closed,
                "close_date": str(deal.close_date) if deal.close_date is not None else None,
                "owner": deal.owner.name if deal.owner is not None else None,
            })

        self.assertEqual(self.deals_test_data(), formatted_deals)

    @db_session
    def test_deals_model(self):
        deals = select(deal for deal in Deal)
        formatted_deals = [deal.get_formatted_data() for deal in deals]

        self.assertEqual(self.deals_test_data(), formatted_deals)
