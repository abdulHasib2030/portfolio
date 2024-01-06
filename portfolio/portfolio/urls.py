
from django.contrib import admin
from django.urls import path, include
from first_app.views import home, contactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('contact/', contactView, name = 'contact'),
]
