from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ReportListCreate.as_view(), name='report_list'),

]