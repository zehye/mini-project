from django.urls import path


from products.views import exhibition_total_list

urlpatterns = [
    path('exhibition/', exhibition_total_list, name='exhibition')
]