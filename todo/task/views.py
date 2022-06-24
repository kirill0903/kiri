from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from task.models import Task


def index(request):
	return HttpResponse('Hello, world!')


def get_all_tasks(request):
	context = {
		'tasks': Task.objects.order_by('status', '-id'),
		'title': 'All tasks'
	}
	return render(request, 'all.html', context)
	# tasks = Task.objects.order_by('status', '-id')
	# response = f'<h1>Всего задач найдено {len(tasks)}<br></h1>'
	# for task in tasks:
	# 	response += f'{task.title} {task.status}<br>'
	# return HttpResponse(response)


def get_all_tasks_by_status(request, status):
	tasks = Task.objects.filter(status=status)
	response = f'<h1>Всего задач найдено {len(tasks)}<br></h1>'
	for task in tasks:
		response += f'{task.title}<br>'
	return HttpResponse(response)


def get_task_detail(request, task_id):
	try:
		task = Task.objects.get(id=task_id)
	except Task.DoesNotExist:
		return HttpResponse(f'Задачи с номером {task_id} не существует!')
	context = {
		'title': task.title,
		'task': task
	}
	return render(request, 'detail.html', context)


"""
Задание:

Создать приложение articles с помощью команды python manage.py startapp articles
Создать модель Article с полями:
 * id
 * title
 * content
 * creator_name
 * updated_at
 * created_at

Создать 2 запроса
/articles - который возвращает заголовки всеъ статей
/articles/detail/<int:article_id> - который возвращает content статьи по ид

Код необходимо загрузить в github репозиторий
"""

