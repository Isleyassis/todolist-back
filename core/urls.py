from django.urls import path
from .views import taskList, taskView, create_task

urlpatterns = [
  path('', taskList, name='task-list'),
  path('task/<int:id>', taskView, name='task-view'),
  path('task/create', create_task, name='create-task')
]
