from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.SegDataListCreate.as_view(), name='seg_data_list'),
]