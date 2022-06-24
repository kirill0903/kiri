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
		return f'{self.id} {self.title}'


class Rating(models.Model):
	id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=255)
	point = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField(max_length=200)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)