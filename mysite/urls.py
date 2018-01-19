from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('wishlist/', include('wishlist.urls')),
    path('admin/', admin.site.urls),
]