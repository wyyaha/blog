from django.urls import path

from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('categories/<int:pk>/', views.categories, name='categories'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]