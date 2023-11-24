from django.db.models import QuerySet
import datetime




class OrderQuerySet(QuerySet):
    def by_customer(self, customer):
        return self

    def total_price(self):
        orders = self.all()
        orders_total_price = list(orders.values_list('total_price',flat=True))
        total_price =0
        for x in orders_total_price:
            total_price = total_price + x
        print(total_price)
        return total_price

    def total_price_by_customer(self, customer):
        orders =self.filter(customer =customer)
        orders_detail = list(orders.values_list('total_price',flat=True))
        print(orders_detail)
        total_price_by_customer = 0
        for x in orders_detail:
            total_price_by_customer = total_price_by_customer + x
        print(total_price_by_customer)
        return total_price_by_customer

    def submitted_in_date(self, date_value):
        date1=self.filter(date__date = datetime.date(2022,1,1))
        # date2=self.filter(date__date = datetime.date(2022,1,2))

        # date_value = [datetime.date(2022,1,1),datetime.date(2022,1,2)]
        # for x in date_value:
        #     date1=(self.filter(date__date = x).values_list())
        #     print(date1,'%%%%%%%%%%%%')
        return date1
