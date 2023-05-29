from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

class ProductUser(models.Model):
    id
    user_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'product_id'], name='user_product_unique')
        ]