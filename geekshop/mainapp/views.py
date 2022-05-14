from django.shortcuts import render

content = {
    'main_menu': [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]

}


def main(request):
    # own_content = {
    #     'title': title,
    # }
    # content.update(own_content)
    return render(request, 'mainapp/index.html', content)


def products(request):
    # own_content = {
    #     'title': title,
    #     'links_menu': links_menu,
    #     'same_products': same_products,
    # }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    # own_content = {
    #     'title': title,
    # }
    return render(request, 'mainapp/contact.html', content)


def tmp_url(request):
    own_content = {
        'title': "магазин",
    }
    content.update(own_content)
    return render(request, 'mainapp/new_index.html', content)
