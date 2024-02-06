from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from ecommerce_db_auth.models import Products
from .forms import *
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import (
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    CreateView,
)

# Create your views here.


# Class Base Generic
class ListProductGeneric(ListView):
    model = Products
    context_object_name = "productsList"  # context var name
    template_name = "ecommerce_db_auth/mainProducts.html"



class CreateProductGeneric(CreateView):
    model = Products
    context_object_name = "form"  # context var name
    form_class = ProductForm  # if use custom Form
    template_name = "ecommerce_db_auth/mainAddNewProduct.html"
    success_url = reverse_lazy("Products")


class DetailProductGeneric(DetailView):
    model = Products
    context_object_name = "product"  # context var name
    template_name = "ecommerce_db_auth/mainDetailsProduct.html"


class UpdateProductGeneric(UpdateView):
    model = Products
    context_object_name = "form"  # context var name
    form_class = ProductForm  # if use custom Form
    template_name = "ecommerce_db_auth/mainUpdateProduct.html"
    success_url = reverse_lazy("Products")


class DeleteProductGeneric(DeleteView):
    model = Products
    context_object_name = "product"  # context var name
    template_name = "ecommerce_db_auth/mainDeleteProduct.html"
    success_url = reverse_lazy("Products")


# Class View
# class UpdateProduct(View):

#     def get(self, request, productID):
#         print("get class based view")
#         product = Products.getProductDetails(productID)
#         form = ProductForm(instance=product)
#         context = {"form": form}
#         return render(request, "ecommerce_db_auth/mainUpdateProduct.html", context)

#     def post(self, request, productID):
#         print("post class based view")
#         product = Products.getProductDetails(productID)
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid:
#             productObj = form.save()
#             return HttpResponseRedirect("/")


# Function
# http-request ,return http-response
# def listProducts(request):
#     context = {"productsList": Products.getAllProducts()}
#     return render(request, "ecommerce_db_auth/mainProducts.html", context)


# def addNewProduct(request):
#     form = ProductForm()
#     context = {"form": form}
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid:
#             productObj = form.save()
#             return HttpResponseRedirect("/")
#         else:
#             context["MSG"] = "Data Is Not Complete"
#     return render(request, "ecommerce_db_auth/mainAddNewProduct.html", context)


# def updateProduct(request, productID):
#     product = Products.getProductDetails(productID)
#     form = ProductForm(instance=product)
#     context = {"form": form}
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid:
#             productObj = form.save()
#             return HttpResponseRedirect("/")
#         else:
#             context["MSG"] = "Data Is Not Complete"
#     return render(request, "ecommerce_db_auth/mainUpdateProduct.html", context)


# def detailsProduct(request, productID):
#     context = {"product": Products.getProductDetails(productID)}
#     return render(request, "ecommerce_db_auth/mainDetailsProduct.html", context)


# def deleteProduct(request, productID):
#     Products.deleteProduct(id=productID)
#     return HttpResponseRedirect("/")


def category(request):
    context = {"productsList": Products.getAllProducts()}
    return render(request, "ecommerce_db_auth/mainCategory.html", context)


def aboutUS(request):
    return render(request, "ecommerce_db_auth/mainAboutUs.html")


# Category
# Class View
class AddCategory(View):

    def get(self, request):
        print("get class based view")
        form = CategoryForm()
        context = {"form": form}
        return render(request, "ecommerce_db_auth/mainAddNewCategory.html", context)

    def post(self, request):
        print("post class based view")
        form = CategoryForm(request, request.POST, request.FILES)
        if form.is_valid:
            Category.objects.create(
                name=request.POST["name"],
                image=request.FILES["image"],
            )
            return HttpResponseRedirect("/")


# def addNewCategory(request):
#     form = CategoryForm()
#     context = {"form": form}
#     if request.method == "POST":
#         form = CategoryForm(request, request.POST, request.FILES)
#         if form.is_valid:
#             Category.objects.create(
#                 name=request.POST["name"],
#                 image=request.FILES["image"],
#             )
#             return HttpResponseRedirect("/")
#         else:
#             context["MSG"] = "Data Is Not Complete"
#     return render(request, "ecommerce_db_auth/mainAddNewCategory.html", context)
