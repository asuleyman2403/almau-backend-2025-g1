from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    amount = models.IntegerField(null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f'ID: {self.id} {self.title}'



