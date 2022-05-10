from django.shortcuts import render

content = {
    'links_main_menu': [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]
    # 'title': title,
    # 'links_menu': links_menu,
    # 'same_products': same_products
}


def main(request):
    return render(request, 'mainapp/index.html', content)


def products(request):
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', content)


def tmp_url(request):
    return render(request, 'mainapp/new_index.html', content)
