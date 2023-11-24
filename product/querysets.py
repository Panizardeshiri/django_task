from django.db.models import QuerySet


class ProductQuerySet(QuerySet):
    def needs_restock(self):
        """returns a queryset of products that their stock is less than 10"""
        products_need_stock = self.filter(stock__lt=10)
        return products_need_stock
    
    
    def in_stock(self):
        return self
    
    

