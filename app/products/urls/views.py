from django.urls import path


from products.views import exhibition_total_list, exhibition_detail

app_name = 'products'
urlpatterns = [
    path('', exhibition_total_list, name='exhibition'),
    path('<int:pk>/', exhibition_detail, name='exhibition-detail'),
]