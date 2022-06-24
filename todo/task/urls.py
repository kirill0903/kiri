from django.urls import path

from task import views

urlpatterns = [
    path('', views.index, name='index'),  # localhost:8000/tasks/
    path('all', views.get_all_tasks),  # localhost:8000/tasks/all
    path('all/<str:status>', views.get_all_tasks_by_status),  # localhost:8000/tasks/all/open
    path('detail/<int:task_id>', views.get_task_detail)  # localhost:8000/tasks/detail/13
	# path('путь', views.функция, имя_запроса)
]
