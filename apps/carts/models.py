from django.conf import settings
from django.db import models



class ProductCard(models.Model):

    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    shipping = models.PositiveSmallIntegerField(default=8, blank=False, null=True)




    class Meta:
        unique_together = (('user', 'product'),)
