from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('contact.html', views.contact, name="contact"),
    path('booking.html', views.booking, name="booking"),
    path('about.html', views.about, name="about"),
    path('thanks', views.thanks, name='thanks'),
]
