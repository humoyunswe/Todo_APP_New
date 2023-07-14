from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='todo-index'),
    path('add/',views.create_todo,name='todo-create_todo'),
    path('qrcode/<int:todo_id>/', views.generate_qrcode, name='todo-generate_qrcode'),
]


