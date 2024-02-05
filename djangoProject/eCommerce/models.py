from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.


class Products(models.Model):
    # email = models.EmailField()
    # create_date = models.DateTimeField(default=now)
    # update_date = models.DateTimeField(default=now)

    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    rating = models.IntegerField(default=0, null=True)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    categoryImage = models.CharField(max_length=200)


# obj1 = Products(
#     title="iPhone 14 Pro",
#     image="images/products/phone2.png",
#     description="Apple iPhone 14 with FaceTime - 128GB, 4GB RAM, 4G LTE, Black, Single SIM & E-SIM",
#     rating=3,
#     price=39990,
#     category="phone",
#     categoryImage="images/category/smartphone.png",
# )
# obj1.save()

# Products.objects.create(
#     image="images/products/phone4.png",
#     title="iPhone 13 Pro",
#     description="iPhone 13 Pro (128 GB) - Yellow, Bluetooth,  Wi-Fi, USB",
#     rating=4,
#     price=45590,
#     category="phone",
#     categoryImage="images/category/smartphone.png",
# )


# Products.objects.create(image="images/products/phone3.png",title="Xiaomi Redmi 10",description="Xiaomi Redmi 10 Dual SIM Mobile- 6.53 Inch FHD , 64GB, 4GB RAM, 4G LTE - Carbon Gray",rating=2,price=7990,category="phone",categoryImage="images/category/smartphone.png")
