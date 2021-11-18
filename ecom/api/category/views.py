# from django.shortcuts import render

from rest_framework import viewsets

from .serializers import CategorySerializer
from .models import Category


# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    # here we actully mention the two things
    # 1 - what is the query that means what is the data we are
    # bringing from the database
    # 2 - based on the serializer that we have wwritten that data
    # is gonna converted into JSON
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
