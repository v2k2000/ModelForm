from django.urls import path
from . import views

app_name = 'articles'

urlpatterns =[
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete/',views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),
]