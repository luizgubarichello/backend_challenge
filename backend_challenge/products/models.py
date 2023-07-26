from django.db import models

class Product(models.Model):
    code = models.BigIntegerField(primary_key=True)
    barcode = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('imported', 'Imported')])
    imported_t = models.DateTimeField()
    url = models.URLField()
    product_name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50)
    categories = models.CharField(max_length=1000)
    packaging = models.CharField(max_length=1000)
    brands = models.CharField(max_length=1000)
    image_url = models.URLField()

    def __str__(self):
        return self.product_name
