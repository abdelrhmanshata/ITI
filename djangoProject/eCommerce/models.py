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


# productsList = [
#     {
#         "id": 1,
#         "image": "images/products/phone2.png",
#         "title": "iPhone 14 Pro",
#         "description": "Apple iPhone 14 with FaceTime - 128GB, 4GB RAM, 4G LTE, Black, Single SIM & E-SIM",
#         "rating": 3,
#         "price": 39990,
#         "category": "phone",
#         "categoryImage": "images/category/smartphone.png",
#     },
#     {
#         "id": 2,
#         "image": "images/products/phone4.png",
#         "title": "iPhone 13 Pro",
#         "description": "iPhone 13 Pro (128 GB) - Yellow, Bluetooth,  Wi-Fi, USB",
#         "rating": 4,
#         "price": 45590,
#         "category": "phone",
#         "categoryImage": "images/category/smartphone.png",
#     },
#     {
#         "id": 3,
#         "image": "images/products/phone3.png",
#         "title": "Xiaomi Redmi 10",
#         "description": "Xiaomi Redmi 10 Dual SIM Mobile- 6.53 Inch FHD , 64GB, 4GB RAM, 4G LTE - Carbon Gray",
#         "rating": 2,
#         "price": 7990,
#         "category": "phone",
#         "categoryImage": "images/category/smartphone.png",
#     },
#     {
#         "id": 4,
#         "image": "images/products/smartwatch1.png",
#         "title": "Apple Watch SE",
#         "description": "Apple Watch SE GPS 44MM Starlight Aluminum Case with Starlight Sport Band (2nd Gen - 2022)",
#         "rating": 5,
#         "price": 14999,
#         "category": "smartwatch",
#         "categoryImage": "images/category/smart-watch.png",
#     },
#     {
#         "id": 5,
#         "image": "images/products/smartwatch3.png",
#         "title": "HUAWEI WATCH GT 3",
#         "description": "HUAWEI WATCH GT 3 SE Smartwatch, Sleek and Stylish, Science-based Workouts, Sleep Health Monitoring.",
#         "rating": 3,
#         "price": 6459,
#         "category": "smartwatch",
#         "categoryImage": "images/category/smart-watch.png",
#     },
#     {
#         "id": 6,
#         "image": "images/products/smartwatch4.png",
#         "title": "Amazfit GTR 3 Pro",
#         "description": "Amazfit GTR 3 Pro Smart Watch for Android iPhone with Bluetooth Call Alexa GPS WiFi, Men's Fitness Tracker 150 Sports Modes, 1.45”AMOLED Display, Brown",
#         "rating": 4,
#         "price": 7759,
#         "category": "smartwatch",
#         "categoryImage": "images/category/smart-watch.png",
#     },
#     {
#         "id": 7,
#         "image": "images/products/smartwatch5.png",
#         "title": "Ultra Smartwatch 8",
#         "description": "Delone Smart Watch Ultra Smartwatch 8 Series 2” HD Screen Customize Dial Large Capacity Battery IP68 Waterproof (Orange)",
#         "rating": 2,
#         "price": 1200,
#         "category": "smartwatch",
#         "categoryImage": "images/category/smart-watch.png",
#     },
#     {
#         "id": 8,
#         "image": "images/products/earphone1.png",
#         "title": "Xiaomi Buds 3 Active",
#         "description": "Xiaomi Buds 3 Active Noise Cancelling modes Dual device connectivity Supports Wireless charging 32h Long battery life with Charging Case Carbon Black, 480",
#         "rating": 2,
#         "price": 2450,
#         "category": "earphone",
#         "categoryImage": "images/category/earphones.png",
#     },
#     {
#         "id": 9,
#         "image": "images/products/earphone2.png",
#         "title": "New bose quietcomfort 45",
#         "description": "New bose quietcomfort 45 bluetooth wireless noise canceling headphones - triple black",
#         "rating": 4,
#         "price": 9999,
#         "category": "earphone",
#         "categoryImage": "images/category/earphones.png",
#     },
#     {
#         "id": 10,
#         "image": "images/products/earphone3.png",
#         "title": "HUAWEI WATCH GT 3 ",
#         "description": "HUAWEI WATCH GT 3 SE Smartwatch, Sleek and Stylish, Science-based Workouts, Sleep Health Monitoring.",
#         "rating": 3,
#         "price": 6459,
#         "category": "earphone",
#         "categoryImage": "images/category/earphones.png",
#     },
#     {
#         "id": 11,
#         "image": "images/products/earphone4.png",
#         "title": "Amazfit GTR 3 Pro",
#         "description": "Amazfit GTR 3 Pro Smart Watch for Android iPhone with Bluetooth Call Alexa GPS WiFi, Men's Fitness Tracker 150 Sports Modes, 1.45”AMOLED Display, Brown",
#         "rating": 5,
#         "price": 7759,
#         "category": "earphone",
#         "categoryImage": "images/category/earphones.png",
#     },
#     {
#         "id": 12,
#         "image": "images/products/earphone5.png",
#         "title": "Ultra Smartwatch 8",
#         "description": "Delone Smart Watch Ultra Smartwatch 8 Series 2” HD Screen Customize Dial Large Capacity Battery IP68 Waterproof (Orange)",
#         "rating": 2,
#         "price": 1200,
#         "category": "earphone",
#         "categoryImage": "images/category/earphones.png",
#     },
# ]


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
