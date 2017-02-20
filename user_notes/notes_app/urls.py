from django.conf.urls import url
from . import views

app_name = 'notes_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^success/', views.LoginSuccess.as_view(), name='success'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logout/', views.logout_user, name='logout'),
]