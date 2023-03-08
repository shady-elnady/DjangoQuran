from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request= request, template_name= "index.html")

def about(request):
    return render(request= request, template_name= "about.html")

def brand(request):
    return render(request= request, template_name= "brand.html")

def contact(request):
    return render(request= request, template_name= "contact.html")

def special(request):
    return render(request= request, template_name= "special.html")