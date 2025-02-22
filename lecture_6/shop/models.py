from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=255, null=False, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    amount = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'ID: {self.id} {self.title}'






