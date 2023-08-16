from django.urls import path

from catalog.views import home, contact, product_page

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('product/<int:product_id>/', product_page, name='product'),
]
