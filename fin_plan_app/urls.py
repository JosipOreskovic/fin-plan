"""Defines URL patterns for fin_plan_app."""

from django.urls import path
from . import views

app_name = 'fin_plan_app'
urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	#Page that shows all clients
	path('clients', views.clients, name='clients'),
	#Detail page for single client
	path('clients/<int:client_id>/', views.client, name='client'),
	#Page for adding a new client
	path('new_client/', views.new_client, name='new_client'),
	#Page for adding a new task.
	path('new_task/<int:client_id>/', views.new_task, name='new_task'),
	#Page for adding a new note.
	path('new_note/<int:client_id>/', views.new_note, name='new_note'),
	#Page for editing a client
	path('edit_client/<int:client_id>/', views.edit_client, name='edit_client'),
	#Page for editing a task
	path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
	# Page for editing a note
	path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
	#Page for deleting a client
	path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
	#Page for deleting a task
	path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
	#Page for deleting a task
	path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
	#Page that shows all tasks
	path('tasks', views.tasks, name='tasks'),
	#Page that shows all notes
	path('notes', views.notes, name='notes'),
]