from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main_post, name='main_post')
    # path('<int:id>/', views.ImageRetrieveDestroy.as_view(), name='image_retrieve'),
]