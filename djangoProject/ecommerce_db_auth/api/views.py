from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from ecommerce_db_auth.models import *
from .serializer import *


@api_view(["GET", "POST"])
def hello(request):
    # print(request.method)
    print(request.data)
    return Response({"data": request.data})
    # return JsonResponse({"msg": "Hello Abd Elrhman"})


@api_view(["GET"])
def allCategory(request):
    dataCategory = Category.objects.all()
    # dataJson = CategorySerializer(dataCategory, many=True).data
    dataJson = CategorySerializerGeneric(dataCategory, many=True).data
    return Response({"MSG": "All Category", "allCategory": dataJson})


@api_view(["GET"])
def getCategory(request, id):
    category = Category.getCategoryObj(id)
    dataJson = CategorySerializerGeneric(category).data
    return Response({"MSG": "Category Object", "category": dataJson})


@api_view(["POST"])
def addCategory(request):
    # category = CategorySerializer(data=request.data)
    category = CategorySerializerGeneric(data=request.data)
    if category.is_valid():
        category.save()
        return Response({"MSG": "Add Category Done"})
    return Response({"MSG": "Add Category Filed", "Error": category.errors})


@api_view(["PUT", "POST"])
def updateCategory(request, id):
    category = Category.getCategoryObj(id)
    if category:
        # newCategory = CategorySerializer(instance=category, data=request.data)
        newCategory = CategorySerializerGeneric(instance=category, data=request.data)
        if newCategory.is_valid():
            newCategory.save()
            return Response({"MSG": "Update Category Done"})
    return Response({"MSG": "Category Not Found"})


@api_view(["DELETE"])
def deleteCategory(request, id):
    category = Category.objects.filter(id=id)
    if category:
        category.delete()
        return Response({"MSG": "Delete Category Done"})
    return Response({"MSG": "Category Not Found"})
