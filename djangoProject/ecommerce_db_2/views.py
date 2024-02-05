from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from ecommerce_db_2.models import Products
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.


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
        "category": product.category.id,
        "image": product.image,
    }
    form = ProductForm(initial=initial_data)
    context["form"] = form
    if request.method == "POST":
        form = ProductForm(request, request.POST, request.FILES)
        if form.is_valid:
            # Update the fields
            product = Products.objects.get(id=productID)
            if request.POST["image"] != "":
                product.image = request.FILES["image"]
            else:
                product.image = product.image
            product.title = request.POST["title"]
            product.description = request.POST["description"]
            product.rating = int(request.POST["rating"])
            product.price = int(request.POST["price"])
            product.category = Category.getCategoryObj(request.POST["category"])
            # Save the changes
            product.save()

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
