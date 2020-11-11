from django.urls import path
from . import views
urlpatterns=[
    path('todo',views.todo,name='todo'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('delete_todo/<int:item_id>',views.delete_todo,
         name='delete_todo'),
]
