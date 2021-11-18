from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # in the django the image feild dosen't gives full URL thats why we are using imagefield here
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category']
