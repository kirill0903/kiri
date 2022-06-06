from django.db import models


class Task(models.Model):
	OPEN_STATUS = 'open'
	TASK_STATUSES = (
		(OPEN_STATUS, 'Open'),
		('in_progress', 'In progress'),
		('done', 'Done'),
	)

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=40)  # Текстовое поле
	description = models.TextField()  # Текстовое поле
	status = models.CharField(
		max_length=20,
		choices=TASK_STATUSES,
		default=OPEN_STATUS,
	)  # Текстовое поле с возможность выбора
	updated_at = models.DateTimeField(auto_now=True)  # Дата и время которая задается автоматически при изменении записи
	created_at = models.DateTimeField(auto_now_add=True)  # Дата и время которая задается автоматически при создании записи

    def __str__(self):


