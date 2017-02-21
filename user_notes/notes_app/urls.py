from django.conf.urls import url
from .import views

app_name = 'notes_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^my_notes/', views.LoginSuccess.as_view(), name='my_notes'),
    url(r'^new_note/', views.NewNote.as_view(), name='new_note'),
    url(r'^note/(?P<id>\d+)/$', views.note_detail, name='note_detail'),
    url(r'^add_note/', views.add_note, name='add_note'),
    url(r'^register/', views.Register.as_view(), name='register'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^register_user/', views.register_user, name='register_user'),
    url(r'^logout/', views.logout_user, name='logout'),
]