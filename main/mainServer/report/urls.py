from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.report_post, name='report_post')
    # path('<int:id>/', views.ImageRetrieveDestroy.as_view(), name='image_retrieve'),
]