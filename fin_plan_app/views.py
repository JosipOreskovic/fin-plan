from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from datetime import timedelta

from .models import Client, Task, Note
from .forms import ClientForm, TaskForm, NoteForm
# Create your views here.

def index(request):
	"""The home page for fin_plan_app"""
	return render(request, 'fin_plan_app/index.html')

@login_required
def clients(request):
	"""Show all topics"""
	clients = Client.objects.filter(owner=request.user).order_by('name')
	context = {'clients': clients}
	return render(request, 'fin_plan_app/clients.html', context)

@login_required
def tasks(request):
	"""Show all tasks"""
	tasks = Task.objects.filter(owner=request.user).order_by('due_date')
	context = {'tasks': tasks}
	return render(request, 'fin_plan_app/tasks.html', context)

@login_required
def notes(request):
	"""Show all notes"""
	notes = Note.objects.filter(owner=request.user).order_by('date_added')
	context = {'notes': notes}
	return render(request, 'fin_plan_app/notes.html', context)

@login_required
def client(request, client_id):
	"""Show a single client and all its taks"""
	client = get_object_or_404(Client, id=client_id)
	# Make sure the client belongs to current user.
	if client.owner !=request.user:
		raise Http404
	tasks = client.task_set.order_by('-due_date')
	notes = client.note_set.order_by('-date_added')
	context = {'client': client, 'tasks': tasks, 'notes': notes}
	return render(request, 'fin_plan_app/client.html', context)

@login_required
def new_client(request):
	"""Add a new client"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ClientForm()
	else:
		# POST data submitted; process data.
		form = ClientForm(data=request.POST)
		if form.is_valid():
			new_client = form.save(commit=False)
			new_client.owner = request.user
			new_client.save()
			return redirect('fin_plan_app:clients')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'fin_plan_app/new_client.html', context)

@login_required
def new_task(request, client_id):
	"""Add a new task for praticular client"""
	client = Client.objects.get(id=client_id)

	if request.method !='POST':
		#No data submitted; create blank form
		form = TaskForm()
	else:
		#POST data submitted; process data
		form = TaskForm(data=request.POST)
		if form.is_valid():
			new_task = form.save(commit=False)
			new_task.owner = request.user
			new_task.client = client
			new_task.save()
			
			if new_task.recurring  == '1':
				delta =  new_task.end_date - new_task.due_date
				step = timedelta(weeks = 1)
				due_date_delta = step
				while due_date_delta < delta:
					form = TaskForm(data=request.POST)
					new_task = form.save(commit=False)
					new_task.owner = request.user
					new_task.client = client
					new_task.due_date = new_task.due_date + due_date_delta
					new_task.save()
					due_date_delta += step
			return redirect('fin_plan_app:client', client_id=client.id)

	#Display a blank or invalid form
	context = {'client': client, 'form': form}
	return render(request, 'fin_plan_app/new_task.html', context)

@login_required
def new_note(request, client_id):
	"""Add a new note for praticular client"""
	client = Client.objects.get(id=client_id)

	if request.method !='POST':
		#No data submitted; create blank form
		form = NoteForm()
	else:
		#POST data submitted; process data
		form = NoteForm(data=request.POST)
		if form.is_valid():
			new_note = form.save(commit=False)
			new_note.owner = request.user
			new_note.client = client
			new_note.save()
			return redirect('fin_plan_app:client', client_id=client.id)

	#Display a blank or invalid form
	context = {'client': client, 'form': form}
	return render(request, 'fin_plan_app/new_note.html', context)

@login_required
def edit_client(request, client_id):
	"""Edit an existing client"""
	client = Client.objects.get(id=client_id)
	if client.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request; pre-fill form with the current task
		form = ClientForm(instance=client)
	else:
		#POST data submitted; process data
		form = ClientForm(instance=client, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('fin_plan_app:clients')

	context = {'client': client, 'form': form}
	return render(request, 'fin_plan_app/edit_client.html', context)

@login_required
def edit_task(request, task_id):
	"""Edit an existing task"""
	task = Task.objects.get(id=task_id)
	client = task.client
	if client.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request; pre-fill form with the current task
		form = TaskForm(instance=task)
	else:
		#POST data submitted; process data
		form = TaskForm(instance=task, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('fin_plan_app:client', client_id=client.id)

	context = {'task': task, 'client': client, 'form': form}
	return render(request, 'fin_plan_app/edit_task.html', context)

@login_required
def edit_note(request, note_id):
	"""Edit an existing task"""
	note = Note.objects.get(id=note_id)
	client = note.client
	if client.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request; pre-fill form with the current task
		form = NoteForm(instance=note)
	else:
		#POST data submitted; process data
		form = NoteForm(instance=note, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('fin_plan_app:client', client_id=client.id)

	context = {'note': note, 'client': client, 'form': form}
	return render(request, 'fin_plan_app/edit_note.html', context)

@login_required
def delete_client(request, client_id):
	"""Delete an existing client"""
	client = Client.objects.get(id=client_id)
	client.delete()
	return redirect ('fin_plan_app:clients')

@login_required
def delete_task(request, task_id):
	"""Delete an existing task"""
	task = Task.objects.get(id=task_id)
	client = task.client
	task.delete()
	return redirect ('fin_plan_app:client', client_id=client.id)

@login_required
def delete_note(request, note_id):
	"""Delete an existing task"""
	note = Note.objects.get(id=note_id)
	client = note.client
	note.delete()
	return redirect ('fin_plan_app:client', client_id=client.id)

