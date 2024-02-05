from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProductForm(forms.Form):
    title = forms.CharField(max_length=30, required=True)
    description = forms.CharField(max_length=300, required=True)
    rating = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)
    category = forms.ChoiceField(choices=Category.getCATEGORY_CHOICES())
    image = forms.ImageField(required=True)

    def clean_name(self):
        pTitle = self.cleaned_data["title"]
        obj = Products.objects.filter(title=pTitle).exists()
        if obj:
            raise ValidationError("Title Must be Unique")
        else:
            return True


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    image = forms.ImageField(required=True)

    def clean_name(self):
        cName = self.cleaned_data["name"]
        obj = Category.objects.filter(name=cName).exists()
        if obj:
            raise ValidationError("Title Must be Unique")
        else:
            return True
