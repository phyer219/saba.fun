from django.urls import path

from . import views

app_name = 'poetry'
urlpatterns = [
    path('', views.index, name='index'),
    path('shijing/', views.shijing, name='shijing'),
    path('shijing/<int:shijing_id>/', views.shijing_id, name='shijing_id'),
    path('ci/', views.ci, name='ci'),
    path('ci/<int:ci_aut_id>', views.ci_aut_id, name='ci_aut_id'),

]
