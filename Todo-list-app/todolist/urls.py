from django.conf.urls import url
from todolist import views

urlpatterns = [
	url(r'^home/$', views.listItems, name='home'),
	url(r'^getitem/$', views.getItems, name='get_item'),
	url(r'^makelist/$', views.buildList, name='build_list'),
	url(r'^initremove/$', views.removeTask_init, name='remove_task_init'),
	url(r'^remove/$',views.removeTask, name='remove_task'),
]
