# api_root\urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('api.urls'), name='api_urls')
    # path('', include('api.urls'), name='api_urls')
    path('api/', include('api.urls'))
        
]