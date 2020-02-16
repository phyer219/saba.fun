from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('editormd', views.editormd, name='editormd')
#    path('shijing/', views.shijing, name='shijing'),
]
