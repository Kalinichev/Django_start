from django.shortcuts import render

content = {}


def main(request):
    return render(request, 'mainapp/index.html', content)


def products(request):
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html', content)


def tmp_url(request):
    return render(request, 'mainapp/base.html')
