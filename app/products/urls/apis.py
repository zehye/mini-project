from django.urls import path

from products import apis

urlpatterns = [
    path('exhibition/', apis.ExhibitionList.as_view()),
]