from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    return render(request= request, template_name= "index.html")

@login_required
def about(request):
    return render(request= request, template_name= "about.html")

@login_required
def brand(request):
    return render(request= request, template_name= "brand.html")

@login_required
def contact(request):
    return render(request= request, template_name= "contact.html")

@login_required
def special(request):
    return render(request= request, template_name= "special.html")