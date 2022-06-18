from django.shortcuts import render
from .models import Product, ProductCategory

content = {
    'main_menu': [
        {'href': 'shop:main', 'name': 'домой'},
        {'href': 'shop:products', 'name': 'продукты'},
        {'href': 'shop:contact', 'name': 'контакты'},
    ]

}


def main(request):
    title = 'Главная'
    products = Product.objects.all()

    own_content = {
        'title': title,
        'products': products,
    }
    content.update(own_content)
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    own_content = {
        'title': 'продукты',
        'links_menu': links_menu,
        # 'same_products': same_products,
    }

    content.update(own_content)
    return render(request, 'mainapp/products.html', content)


def contact(request):
    own_content = {
        'title': 'контакты',
    }
    content.update(own_content)
    return render(request, 'mainapp/contact.html', content)

