from django.urls import path
from .views import UserEditView, get_or_create_profile, signup, myprofile
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    path('myprofile/', get_or_create_profile, name='myprofile'),
    path('myprofile/', myprofile, name='myprofile'),
    path("customer_service", views.contact, name="customer_service"),
]
