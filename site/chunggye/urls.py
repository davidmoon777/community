from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site.urls')),  # 단일 사이트 URL 연결
]
