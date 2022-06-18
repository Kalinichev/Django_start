from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import get_object_or_404

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
    print(pk)

    title = 'продукты'
    # links_menu = [
    #     {'href': 'products_all', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]

    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)

        own_content = {
            'title': title,
            'links_menu': links_menu,
            'products': products,
            'category': category,
        }

        content.update(own_content)
        return render(request, 'mainapp/products.html', content)

    same_products = Product.objets.all()[3:5]

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
