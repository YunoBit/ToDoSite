from django.urls import path 

from apps.todos import views


urlpatterns = [
    path('', views.homepage , name = 'index'),
    path('create/', views.create , name = 'create'),
    path('detail/<int:pk>/',views.retrieve, name = 'detail'),
    path('update/<int:pk>', views.update, name = 'update'),
    path('delete/<int:pk>', views.distroy, name = 'distroy'),
    path('done/', views.done_tasks, name='done_tasks'),
    path('add_done/<int:pk>', views.done_tasks_add, name="add_done"),
]