from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


englishAppFolder = "islamic_center_app/English"

arabicAppFolder = "islamic_center_app/Arabic"



@login_required
def arabicHome(request):
    return render(request= request, template_name= f"{arabicAppFolder}/index_rtl.html")


@login_required
def home(request):
    return render(request= request, template_name= f"{englishAppFolder}/index.html")

@login_required
def about(request):
    return render(request= request, template_name= f"{englishAppFolder}/about.html")

@login_required
def blogDetail(request):
    return render(request= request, template_name= f"{englishAppFolder}/blog-dtail.html")

@login_required
def blog(request):
    return render(request= request, template_name= f"{englishAppFolder}/blog.html")

@login_required
def comingSoon(request):
    return render(request= request, template_name= f"{englishAppFolder}/comingsoon.html")

@login_required
def contact(request):
    return render(request= request, template_name= f"{englishAppFolder}/contact.html")

@login_required
def crowdFundingDetail(request):
    return render(request= request, template_name= f"{englishAppFolder}/crowd-funding-detail.html")

@login_required
def crowdFunding(request):
    return render(request= request, template_name= f"{englishAppFolder}/crowd-funding.html")

@login_required
def donation(request):
    return render(request= request, template_name= f"{englishAppFolder}/donation.html")

@login_required
def errorPage(request):
    return render(request= request, template_name= f"{englishAppFolder}/error-page.html")

@login_required
def events(request):
    return render(request= request, template_name= f"{englishAppFolder}/events.html")

@login_required
def eventDetail(request):
    return render(request= request, template_name= f"{englishAppFolder}/event-detail.html")

@login_required
def galleryMedium(request):
    return render(request= request, template_name= f"{englishAppFolder}/gallery-medium.html")

@login_required
def gallerySmall(request):
    return render(request= request, template_name= f"{englishAppFolder}/gallery-small.html")

@login_required
def product(request):
    return render(request= request, template_name= f"{englishAppFolder}/product.html")

@login_required
def productDetail(request):
    return render(request= request, template_name= f"{englishAppFolder}/product-detail.html")

@login_required
def scholars(request):
    return render(request= request, template_name= f"{englishAppFolder}/scholars.html")

@login_required
def searchResult(request):
    return render(request= request, template_name= f"{englishAppFolder}/search-result.html")