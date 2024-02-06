from django.db import models
from datetime import datetime
from django.utils.timezone import now


# Create your models here.
class User(models.Model):
    pass 


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/category/", blank=True, null=True)

    def __str__(self):
        return self.name

    def getCategoryImageUrl(self):
        return f"/media/{self.image}"

    @classmethod
    def getCATEGORY_CHOICES(cls):
        return [(category.id, category.name) for category in cls.objects.all()]

    @classmethod
    def getCategoryObj(cls, cID):
        return cls.objects.get(id=cID)


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    rating = models.IntegerField(default=1, null=True)
    price = models.IntegerField(default=1)
    # object  os Category
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/products/", blank=True, null=True)

    def __str__(self):
        return self.title

    def getImageUrl(self):
        return f"/media/{self.image}"

    @classmethod
    def getAllProducts(cls):
        return cls.objects.all()

    @classmethod
    def getProductDetails(cls, pID):
        return cls.objects.get(id=pID)

    @classmethod
    def deleteProduct(cls, pID):
        return cls.objects.filter(id=pID).delete()
