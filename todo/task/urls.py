from django.urls import path
from .views import get_tasks,add_task,update_task,delete_task,edit_task


urlpatterns = [
    path('task/', get_tasks, name='task_list'),            # GET — список
    path('task/add/', add_task, name='task_add'),         # POST — добавление
    path('task/<int:id>/edit/', edit_task, name='task_edit'),   # GET — форма редактирования
    path('task/<int:id>/update/', update_task, name='task_update'),  # POST — обновление
    path('task/<int:id>/delete/', delete_task, name='task_delete'),  # POST — удаление
]