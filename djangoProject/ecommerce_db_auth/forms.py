from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"  # ["nameField,nameField,..."]
        # excludes=['nameField']

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
