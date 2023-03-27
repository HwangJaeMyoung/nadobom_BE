from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ImageListCreate.as_view(), name='image_list'),
    path('<int:id>/', views.ImageRetrieveDestroy.as_view(), name='image_retrieve'),
]