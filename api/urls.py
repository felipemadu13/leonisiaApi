# api\urls.py

from django.contrib import admin
from django.urls import path, include

from api import views

from django.urls import path

from .views import user_login
from .views import user_logout
from .views import user_register

urlpatterns = [
    path('login/', user_login, name='login'),   
    path('logout/', user_logout, name='logout'), 
    path('register/', user_register, name='register'),       
     
    path('servicos', views.get_servicos, name='get_all_servicos'),
    path('servicos/<int:id>', views.get_servicos_by_id, name='get_servicos_by_id'),

    path('servicosrealizados', views.get_servicos_realizados, name='get_all_servicos_realizados'),
    path('servicosrealizados/<int:id>', views.get_servicos_realizados_by_id, name='get_servicos_by_id'),

    path('transacoes', views.get_transacoes, name='transacoes'),
    path('transacoes/<int:id>', views.get_transacoes_by_id, name='transacoes_id'),
]
