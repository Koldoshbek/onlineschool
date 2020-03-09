from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    barcode = models.CharField(max_length=12, unique=True)
    writer = models.CharField(max_length=256)
    published = models.DateField(blank=True, null=True)
    creating_date = models.DateField(auto_now_add=True)
    grade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
