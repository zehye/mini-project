from django.urls import path

from products import apis

urlpatterns = [
    path('', apis.ExhibitionList.as_view()),
]