from django.urls import path

from .. import views

app_name = 'members'
urlpatterns = [
    path('facebook-login/', views.facebook_login, name='facebook-login'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
