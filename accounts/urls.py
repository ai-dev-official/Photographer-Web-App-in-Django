from django.urls import path
from .views import UserEditView, signup, profile
from . import views


#app_name = 'accounts'

urlpatterns = [
    path('register/', signup, name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
    path('profile/', profile, name='profile'),
    path("customer_service", views.contact, name="customer_service"),
]
