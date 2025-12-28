from django.contrib import admin
from django.urls import path, include
from portfolio.views import home  # Импортируем из приложения

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('portfolio/', include('portfolio.urls')),
    path('contacts/', include('contacts.urls')),
]