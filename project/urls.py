from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>', views.detail, name='detail')
]
