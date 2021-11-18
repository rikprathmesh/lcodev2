from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # jsonfollowing = core_serializers.serialize('json', [followiing, ])

    class Meta:
        model = Category
        fields = ['name', 'description']
        # field = '__all__'
        # field = ('name', 'description')

        # exclude = (‘fields’, ‘other’, ‘than’, ‘these’...)..by using
        # this term in stackoverflow
        # exclude = ['name', 'description']
