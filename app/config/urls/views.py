from django.contrib import admin
from django.urls import path, include

from .. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('members/', include('members.urls')),
    path('products/', include('products.urls')),
]
