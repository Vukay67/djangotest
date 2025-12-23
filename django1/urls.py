from django.contrib import admin
from django.urls import path
from core.views import index_views, ret

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views),
    path('ret/', ret)
]
