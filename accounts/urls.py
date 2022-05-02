from django.urls import path
from .views import UserEditView, signup, myprofile
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', signup, name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    path('myprofile/', myprofile, name='myprofile'),
    path("customer_service", views.contact, name="customer_service"),
]
