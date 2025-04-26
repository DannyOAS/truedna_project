from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def how_it_works(request):
    return render(request, 'core/how_it_works.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def faq(request):
    return render(request, 'core/faq.html')

def testimonials(request):
    return render(request, 'core/testimonials.html')

def contact(request):
    return render(request, 'core/contact.html')
