from django.shortcuts import render

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    return render(request, 'catalog/contact.html')


def get_product_info(product_id):
    # Используйте методы модели Product для получения информации о товаре из базы данных
    product = Product.objects.get(id=product_id)
    return product


def product_page(request, product_id):
    # Получите информацию о товаре из базы данных
    product_info = get_product_info(product_id)
    # Передайте информацию о товаре в шаблон
    return render(request, 'product.html', {'product_info': product_info})


