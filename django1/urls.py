from django.contrib import admin
from django.urls import path
from core.views import index_views, cars_views, ret

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views),
    path('cars/', cars_views),
    path('ret/', ret)
]
