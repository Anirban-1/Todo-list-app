from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from todolist.models import MyList
from datetime import datetime, date
from django.core.urlresolvers import reverse
# Create your views here.


def listItems(request):
	# display the items in the todo list
	item_list=MyList.objects.all()
	template_path='todolist/home.html'
	context={
		'item_list':item_list,
	}
	return render(request,template_path,context)

def getItems(request):
	template_path = 'todolist/getitem.html'
	context={}
	return render(request,template_path,context)

def buildList(request):
	# get items from user and build the list
	task=request.POST['task'].upper()
	due_date=request.POST['due_date']
	datetime_obj=datetime.strptime(due_date,"%d-%m-%Y")
	date_obj=datetime_obj.date()
	priority=request.POST['priority']

	new_task = MyList.objects.create(task=task,due_date=date_obj,priority=priority)
	new_task.save()
	return HttpResponseRedirect(reverse('home',args=[]))

def removeTask_init(request):
	template_path = 'todolist/remove.html'
	task_list = MyList.objects.all()
	context = {
		'task_list':task_list,
	}
	return render(request,template_path,context)

def removeTask(request):
	task_id = request.POST['task']
	task=get_object_or_404(MyList,pk=task_id)
	task.delete()
	return HttpResponseRedirect(reverse('home',args=[]))
