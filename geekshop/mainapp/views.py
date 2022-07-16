from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_object_or_404

content = {
    'main_menu': [
        {'href': 'shop:main', 'url': 'main', 'name': 'домой'},
        {'href': 'shop:products', 'url': 'products', 'name': 'продукты'},
        {'href': 'shop:contact', 'url': 'contact', 'name': 'контакты'},
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

    title = 'продукты'

    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        own_content = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category,
        }

        content.update(own_content)
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    own_content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
    }

    content.update(own_content)
    return render(request, 'mainapp/products.html', content)


def contact(request):
    own_content = {
        'title': 'контакты',
    }
    content.update(own_content)
    return render(request, 'mainapp/contact.html', content)
