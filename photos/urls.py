from django.urls import path
from . import views
from .views import editPhoto, deletePhoto, likeView, viewPhoto # PhotoDetailView


urlpatterns = [
    path('', views.gallery, name='gallery'),
    #path('photo/<str:pk>', views.viewPhoto, name='photo'),
    #path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('<int:pk>/edit/', editPhoto.as_view(), name='photo_edit'),
    path('<int:pk>/delete/', deletePhoto.as_view(), name='photo_delete'),
    path('photo/<int:pk>/', viewPhoto, name='photo'),
    path('like/<int:pk>', likeView, name='like_photo'),
]
