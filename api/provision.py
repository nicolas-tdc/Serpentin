import calendar
import datetime
import random

from faker import Faker
from pony.orm import db_session, commit, select

from serpentin.core.database import connect_to_database
from serpentin.models.deals import Deal
from serpentin.models.sales import Sales
from serpentin.models.statements import Statement
from serpentin.models.compensations import Compensation
from serpentin.helpers.compensations import CompensationHelpers

connect_to_database()
fake = Faker("fr-FR")


@db_session
def provision_database():
    for _ in range(5):
        Sales(name=fake.name())
    commit()

    sales = select(s for s in Sales)

    for sale in sales:
        for year in range(2020, 2023):
            for month in range(1, 13):
                month_range = calendar.monthrange(year, month)
                deals_count = 0
                monthly_deals_total = 0
                for _ in range(random.randint(2, 10)):
                    closed = random.random() > 0.5
                    deal_amount = random.randint(10, 50) * 100

                    close_date = None
                    if closed:
                        monthly_deals_total += deal_amount
                        deals_count += 1
                        close_date = fake.date_between(
                            start_date=datetime.date(month=month, year=year, day=1),
                            end_date=datetime.date(
                                month=month, year=year, day=month_range[1]
                            ),
                        )

                    Deal(
                        name=fake.company(),
                        active=True,
                        modified=False,
                        amount=deal_amount,
                        closed=closed,
                        close_date=close_date,
                        owner=sale,
                    )

                statement = Statement(
                    sales=sale,
                    month=month,
                    year=year,
                )

                name = sale.name.replace(' ', '-').lower() + "_" + str(month) + "-" + str(year)
                compensation_type = random.choice(['Simple', 'Complex'])
                draft = random.choice([True, False])
                if compensation_type == 'Simple':
                    amount = CompensationHelpers.calculate_simple_compensation(deals_count, monthly_deals_total)
                elif compensation_type == 'Complex':
                    amount = CompensationHelpers.calculate_complex_compensation(deals_count, monthly_deals_total)
                else:
                    amount = 0

                Compensation(
                    name=name,
                    type=compensation_type,
                    draft=draft,
                    amount=amount,
                    deals_count=deals_count,
                    statement=statement,
                )

    commit()


if __name__ == "__main__":
    provision_database()
