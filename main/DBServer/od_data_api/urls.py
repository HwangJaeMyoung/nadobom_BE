from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.OdDataListCreate.as_view(), name='od_data_list'),
    # path('<int:id>/', views.ImageRetrieveDestroy.as_view(), name='image_retrieve'),
]