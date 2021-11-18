# here we get the 'rest_framework routers' help
from rest_framework import routers
from django.urls import path, include
from . import views

# router = routers.DefaultRouter()
# here is the variety of routers we use the DefaultRouter
# router.register(r'', views.CategoryViewset)
# we declaire empty path here coz awe already mention the path into the api urls
# as path('category/', include('api.category.urls')) if we mention one more time here
# the particular path gonna be like api/category/category

# urlpatterns = [
#     path('', include(router.urls))
# ]


router = routers.DefaultRouter()
router.register(r'', views.CategoryViewset)

urlpatterns = [
    path('', include(router.urls))
]
