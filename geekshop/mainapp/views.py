from django.shortcuts import render

content = {
    'main_menu': [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

}


def main(request):
    own_content = {
        'title': 'магазин',
    }
    content.update(own_content)
    return render(request, 'mainapp/index.html', content)


def products(request):
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


def tmp_url(request):
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
    return render(request, 'mainapp/new_index.html', content)
