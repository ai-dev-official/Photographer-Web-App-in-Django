from django.urls import path
from .views import UserEditView, get_or_create_profile, signup, myprofile
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    path('myprofile/', views.get_or_create_profile, name='myprofile'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path("customer_service", views.contact, name="customer_service"),
]
