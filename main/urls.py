

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('post', views.post, name = 'post'),
    path('success', views.success, name = 'success')
]