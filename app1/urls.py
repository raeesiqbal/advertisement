from django.urls import path
from app1 import views


app_name = "aap1"


urlpatterns = [
    path('',views.home , name='home'),
    path('product-detail/<int:id>',views.product_detail , name='product_detail'),



]