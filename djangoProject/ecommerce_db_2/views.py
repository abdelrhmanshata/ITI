from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from ecommerce_db_2.models import Products
from .forms import *


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


# http-request ,return http-response
def products(request):
    context = {"productsList": Products.productsList()}
    return render(request, "ecommerce_db_2/mainProducts.html", context)


def addNewProduct(request):
    form = ProductForm()
    context = {"form": form}
    if request.method == "POST":
        form = ProductForm(request, request.POST, request.FILES)
        if form.is_valid:
            print(request.POST["category"])
            Products.objects.create(
                image=request.FILES["image"],
                title=request.POST["title"],
                description=request.POST["description"],
                rating=int(request.POST["rating"]),
                price=int(request.POST["price"]),
                category=Category.getCategoryObj(request.POST["category"]),
            )
            # r = reverse("Products")
            # return HttpResponseRedirect(r)
            return HttpResponseRedirect("/")
        else:
            context["MSG"] = "Data Is Not Complete"
    return render(request, "ecommerce_db_2/mainAddNewProduct.html", context)


def productDetails(request, productID):
    context = {"product": Products.productDetails(productID)}
    return render(request, "ecommerce_db_2/mainDetailsProduct.html", context)


def productUpdate(request, productID):
    context = {}
    product = Products.objects.get(id=productID)
    context["product"] = product
    initial_data = {
        "title": product.title,
        "description": product.description,
        "rating": product.rating,
        "price": product.price,
        # "category": product.category,
        # "image": product.image,
    }
    form = ProductForm(initial=initial_data)
    context["form"] = form
    if request.method == "POST":
        form = ProductForm(request, request.POST, request.FILES)
        if form.is_valid:
            Products.objects.filter(id=productID).update(
                image=request.FILES["image"],
                title=request.POST["title"],
                description=request.POST["description"],
                rating=int(request.POST["rating"]),
                price=int(request.POST["price"]),
                category=Category.getCategoryObj(request.POST["category"]),
            )
            # r = reverse("Products")
            # return HttpResponseRedirect(r)
            return HttpResponseRedirect("/")
        else:
            context["MSG"] = "Data Is Not Complete"
    return render(request, "ecommerce_db_2/mainUpdateProduct.html", context)


def deleteProduct(request, productID):
    Products.deleteProduct(id=productID)
    return HttpResponseRedirect("/")


def category(request):
    context = {"productsList": Products.objects.all()}
    return render(request, "ecommerce_db_2/mainCategory.html", context)


def aboutUS(request):
    return render(request, "ecommerce_db_2/mainAboutUs.html")


# Category


def addNewCategory(request):
    form = CategoryForm()
    context = {"form": form}
    if request.method == "POST":
        form = CategoryForm(request, request.POST, request.FILES)
        if form.is_valid:
            Category.objects.create(
                name=request.POST["name"],
                image=request.FILES["image"],
            )
            return HttpResponseRedirect("/")
        else:
            context["MSG"] = "Data Is Not Complete"
    return render(request, "ecommerce_db_2/mainAddNewCategory.html", context)
