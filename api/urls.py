from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('servicos', views.get_servicos, name='get_all_servicos'),
    path('servicos/<int:id>', views.get_servicos_by_id, name='get_servicos_by_id'),
    path('servicosrealizados', views.get_servicos_realizados, name='get_all_servicos_realizados'),
    path('servicosrealizados/<int:id>', views.get_servicos_realizados_by_id, name='get_servicos_by_id'),
]
