from django.urls import path, include
from . import views
urlpatterns = [
    path('check/<int:version>', views.update_check, name='version_check_view'),
    path('execute', views.update_excute, name='update_excute_view'),
    path('test', views.update_excute2, name='update_excute_view2'),
]


