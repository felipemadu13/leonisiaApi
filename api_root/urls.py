from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api_urls'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
]
