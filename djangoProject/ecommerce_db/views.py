from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from ecommerce_db.models import Products
from django.shortcuts import get_object_or_404

# Create your views here.

#
# Data Products
# Products.objects.create(
#     image="images/products/phone2.png",
#     title="iPhone 14 Pro",
#     description="Apple iPhone 14 with FaceTime - 128GB, 4GB RAM, 4G LTE, Black, Single SIM & E-SIM",
#     rating=3,
#     price=39990,
#     category="phone",
#     categoryImage="images/category/smartphone.png",
# )
# Products.objects.create(
#     image="images/products/phone4.png",
#     title="iPhone 13 Pro",
#     description="iPhone 13 Pro (128 GB) - Yellow, Bluetooth,  Wi-Fi, USB",
#     rating=4,
#     price=45590,
#     category="phone",
#     categoryImage="images/category/smartphone.png",
# )
# Products.objects.create(
#     image="images/products/phone3.png",
#     title="Xiaomi Redmi 10",
#     description="Xiaomi Redmi 10 Dual SIM Mobile- 6.53 Inch FHD , 64GB, 4GB RAM, 4G LTE - Carbon Gray",
#     rating=2,
#     price=7990,
#     category="phone",
#     categoryImage="images/category/smartphone.png",
# )
# Products.objects.create(
#     image="images/products/smartwatch1.png",
#     title="Apple Watch SE",
#     description="Apple Watch SE GPS 44MM Starlight Aluminum Case with Starlight Sport Band (2nd Gen - 2022)",
#     rating=5,
#     price=14999,
#     category="smartwatch",
#     categoryImage="images/category/smart-watch.png",
# )
# Products.objects.create(
#     image="images/products/smartwatch3.png",
#     title="HUAWEI WATCH GT 3",
#     description="HUAWEI WATCH GT 3 SE Smartwatch, Sleek and Stylish, Science-based Workouts, Sleep Health Monitoring.",
#     rating=3,
#     price=6459,
#     category="smartwatch",
#     categoryImage="images/category/smart-watch.png",
# )
# Products.objects.create(
#     image="images/products/smartwatch4.png",
#     title="Amazfit GTR 3 Pro",
#     description="Amazfit GTR 3 Pro Smart Watch for Android iPhone with Bluetooth Call Alexa GPS WiFi, Men's Fitness Tracker 150 Sports Modes, 1.45”AMOLED Display, Brown",
#     rating=4,
#     price=7759,
#     category="smartwatch",
#     categoryImage="images/category/smart-watch.png",
# )
# Products.objects.create(
#     image="images/products/smartwatch5.png",
#     title="Ultra Smartwatch 8",
#     description="Delone Smart Watch Ultra Smartwatch 8 Series 2” HD Screen Customize Dial Large Capacity Battery IP68 Waterproof (Orange)",
#     rating=2,
#     price=1200,
#     category="smartwatch",
#     categoryImage="images/category/smart-watch.png",
# )
# Products.objects.create(
#     image="images/products/earphone1.png",
#     title="Xiaomi Buds 3 Active",
#     description="Xiaomi Buds 3 Active Noise Cancelling modes Dual device connectivity Supports Wireless charging 32h Long battery life with Charging Case Carbon Black, 480",
#     rating=2,
#     price=2450,
#     category="earphone",
#     categoryImage="images/category/earphones.png",
# )
# Products.objects.create(
#     image="images/products/earphone2.png",
#     title="New bose quietcomfort 45",
#     description="New bose quietcomfort 45 bluetooth wireless noise canceling headphones - triple black",
#     rating=4,
#     price=9999,
#     category="earphone",
#     categoryImage="images/category/earphones.png",
# )
# Products.objects.create(
#     image="images/products/earphone3.png",
#     title="HUAWEI WATCH GT 3 ",
#     description="HUAWEI WATCH GT 3 SE Smartwatch, Sleek and Stylish, Science-based Workouts, Sleep Health Monitoring.",
#     rating=3,
#     price=6459,
#     category="earphone",
#     categoryImage="images/category/earphones.png",
# )
# Products.objects.create(
#     image="images/products/earphone4.png",
#     title="Amazfit GTR 3 Pro",
#     description="Amazfit GTR 3 Pro Smart Watch for Android iPhone with Bluetooth Call Alexa GPS WiFi, Men's Fitness Tracker 150 Sports Modes, 1.45”AMOLED Display, Brown",
#     rating=5,
#     price=7759,
#     category="earphone",
#     categoryImage="images/category/earphones.png",
# )
# Products.objects.create(
#     image="images/products/earphone5.png",
#     title="Ultra Smartwatch 8",
#     description="Delone Smart Watch Ultra Smartwatch 8 Series 2” HD Screen Customize Dial Large Capacity Battery IP68 Waterproof (Orange)",
#     rating=2,
#     price=1200,
#     category="earphone",
#     categoryImage="images/category/earphones.png",
# )


# Data Products
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


# http-request ,return http-response
def products(request):
    productsListDB = Products.objects.all()
    context = {"productsList": productsListDB}
    return render(request, "ecommerce_db/mainProducts.html", context)


def addProduct(request):
    if request.method == "POST":
        pTitle = request.POST["title"]
        pDescription = request.POST["description"]
        pRating = request.POST["rating"]
        pRating = int(pRating)
        pPrice = request.POST["price"]
        pPrice = int(pPrice)
        pCategory = request.POST["category"]
        pImage = ""
        pCategoryImage = ""
        if pCategory == "phone":
            pImage = "images/products/phone2.png"
            pCategoryImage = "images/category/smartphone.png"
        elif pCategory == "smartwatch":
            pImage = "images/products/smartwatch5.png"
            pCategoryImage = "images/category/smart-watch.png"
        else:
            pImage = "images/products/earphone5.png"
            pCategoryImage = "images/category/earphones.png"

        Products.objects.create(
            image=pImage,
            title=pTitle,
            description=pDescription,
            rating=pRating,
            price=pPrice,
            category=pCategory,
            categoryImage=pCategoryImage,
        )

        return HttpResponseRedirect("/")

    else:
        return render(request, "ecommerce_db/mainAddProduct.html")


def productDetails(request, productID):
    product = Products.objects.get(id=productID)
    context = {"product": product}
    return render(request, "ecommerce_db/mainDetailsProduct.html", context)


def productUpdate(request, productID):
    if request.method == "POST":
        pTitle = request.POST["title"]
        pDescription = request.POST["description"]
        pRating = request.POST["rating"]
        pRating = int(pRating)
        pPrice = request.POST["price"]
        pPrice = int(pPrice)
        pCategory = request.POST["category"]
        pImage = ""
        pCategoryImage = ""
        if pCategory == "phone":
            pImage = "images/products/phone2.png"
            pCategoryImage = "images/category/smartphone.png"
        elif pCategory == "smartwatch":
            pImage = "images/products/smartwatch5.png"
            pCategoryImage = "images/category/smart-watch.png"
        else:
            pImage = "images/products/earphone5.png"
            pCategoryImage = "images/category/earphones.png"

        product = get_object_or_404(Products, id=productID)
        # Update the fields
        product.image = pImage
        product.title = pTitle
        product.description = pDescription
        product.rating = pRating
        product.price = pPrice
        product.category = pCategory
        product.categoryImage = pCategoryImage
        # Save the changes
        product.save()
        return HttpResponseRedirect("/")

    else:
        product = Products.objects.get(id=productID)
        context = {"product": product}
        return render(request, "ecommerce_db/mainUpdateProduct.html", context)


def deleteProduct(request, productID):
    Products.objects.filter(id=productID).delete()
    return HttpResponseRedirect("/")


def category(request):
    productsListDB = Products.objects.all()
    context = {"productsList": productsListDB}
    return render(request, "ecommerce_db/mainCategory.html", context)


def aboutUS(request):
    return render(request, "ecommerce_db/mainAboutUs.html")
