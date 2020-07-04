from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def service1(request):
    return render(request, 'service1.html')


def contact(request):
    return render(request, 'contact.html')


def service2(request):
    return render(request, 'service2.html')


def service3(request):
    return render(request, 'service3.html')


def why_choose_us(request):
    return render(request, 'why_choose_us.html')


def faq(request):
    return render(request, 'faq.html')