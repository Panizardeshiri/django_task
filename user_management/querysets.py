from django.db.models import QuerySet
from order.models import Order

class CustomerQuerySet(QuerySet):
    def annotate_with_total_spending(self):
        total_orders = Order.objects.all()
        customer_id= (list(total_orders.values_list('customer',flat=True)))       
        customer = self.get(id=customer_id[0])
        customer2 = self.get(id='2')
        total_spendings= (list(total_orders.values_list('total_price',flat=True)))
        total_spending =0
        for x in total_spendings:
            total_spending = total_spending + x
        print(total_spending)
        customer.total_spending = total_spending
        customer.save()
        customer2.total_spending = None
        customer2.save()

        return self

    def annotate_with_order_count(self):
        customer1= self.get(id= '1')
        order1 = Order.objects.filter(customer= '1')
        # print(order1.count() , '&&&&&&&&&&&&&')
        customer1.order_count = order1.count()
        customer1.save()
    
        return self