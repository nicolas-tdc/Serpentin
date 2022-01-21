import datetime


class SalesHelpers:

    @staticmethod
    def get_sales_monthly_statement(
            statements, month=datetime.date.today().month, year=datetime.date.today().year, partial=False
    ):
        """
        :param statements: list
        :param month: int
        :param year: int
        :param partial: bool
        :return: Returns statement for a specific month (defaults to current month)
        """
        monthly_statement = {}
        for statement in statements:
            if statement.month == month and statement.year == year:
                monthly_statement = statement.get_partial_data() if partial else statement.get_formatted_data()

        return monthly_statement

    @staticmethod
    def get_sales_last_statements(
            statements, count, start_month=datetime.date.today().month, start_year=datetime.date.today().year
    ):
        """
        Returns n last statements.
        :param statements: list
        :param count: int
        :param start_month: int
        :param start_year: int
        :return: list
        """
        last_statements = []
        dates = []
        for i in range(count):
            if start_month == 0:
                start_month = 12
                start_year -= 1
            dates.append((start_month, start_year))
            start_month -= 1

        for date in dates:
            month, year = date
            last_statements.append(SalesHelpers.get_sales_monthly_statement(statements, month, year))

        return last_statements

    @staticmethod
    def get_sales_deals(deals):
        """
        Returns formatted list of deals for a specific sales.
        :param deals: list
        :return: list
        """
        all_deals = []
        for deal in deals:
            all_deals.append(deal.get_formatted_data())

        return all_deals
