from rest_framework import serializers
from ecommerce_db_auth.models import *


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    image = serializers.ImageField()

    def create(self, validated_data):
        # category = Category()
        # category.name = validated_data["name"]
        # category.image = validated_data["image"]
        # category.save()
        # return category
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.image = validated_data["image"]
        instance.save()
        return instance


class CategorySerializerGeneric(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
