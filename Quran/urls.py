from django.urls import path

from .views import (
    home, about, blogDetail, blog,
    comingSoon, contact, crowdFundingDetail,
    crowdFunding, donation, errorPage,
    events, eventDetail, galleryMedium,
    gallerySmall, product, productDetail,
    scholars, searchResult, arabicHome,
)


app_name = "Quran"


urlpatterns = [
  path('',home, name= "Home"),
  path('ar',arabicHome, name= "ArabicHome"),
  path('about',about, name= "About"),
  path('blog',blog, name= "Blog"),
  path('blog-detail',blogDetail, name= "BlogDetail"),
  path('coming-soon',comingSoon, name= "ComingSoon"),
  path('contact',contact, name= "Contact"),
  path('crowd-funding',crowdFunding, name= "CrowdFunding"),
  path('crowd-funding-detail',crowdFundingDetail, name= "CrowdFundingDetail"),
  path('donation',donation, name= "Donation"),
  path('events',events, name= "Events"),
  path('event-detail',eventDetail, name= "EventDetail"),
  path('gallery-small',gallerySmall, name= "GallerySmall"),
  path('gallery-medium',galleryMedium, name= "GalleryMedium"),
  path('product',product, name= "Product"),
  path('product-detail',productDetail, name= "ProductDetail"),
  path('scholars',scholars, name= "Scholars"),
  path('search-result',searchResult, name= "SearchResult"),
  path('error-page',errorPage, name= "ErrorPage"),
]
