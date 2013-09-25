# encoding: utf8
from todolist.models import Todo, User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url="/login/")
def index(request):
  myTodos = Todo.objects.filter(doers=request.user)
  todosByMe = Todo.objects.filter(author=request.user)
  return render_to_response('index.html', {'user': request.user.username, 'myTodos': myTodos, 'todosByMe': todosByMe})
    
@login_required(login_url="/login/")
def add(request):
  if request.method != 'POST':
    return render_to_response('add.html', {
          'users': User.objects.exclude(username=request.user.username),
          }, context_instance=RequestContext(request))
  else:
    # assert False, request.POST
    try:
      newTodo = Todo.objects.create(caption=request.POST['todocaption'], description=request.POST['tododescription'],
                                    comment=request.POST['todocomment'], author=request.user, pub_date=datetime.datetime.now(),
                                    due_date=datetime.datetime.now())
      for user_id in request.POST.getlist('forwhom'): # you shitty piece of shit
        newTodo.doers.add(User.objects.get(pk=int(user_id)))
      newTodo.save()
    except:
      # assert False, request.POST
      return render_to_response('add.html', {
          'users': User.objects.exclude(username=request.user.username),
          'error_message': u"Что-то пошло не так"
          }, context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect('/')
      
@login_required(login_url="/login/")
def user(request, user_id):
  user = User.objects.get(pk=user_id)
  return render_to_response('user.html', {'user': user.username})
  
@login_required(login_url="/login/")
def edit(request, todo_id):
  todo = Todo.objects.get(pk=todo_id)
  if todo.author == request.user:
    if request.method != 'POST':
      return render_to_response('edit.html', {'todo': todo, 
                                              'users': User.objects.exclude(username=request.user.username),
                                              }, context_instance=RequestContext(request))
    else:
      todo.caption = request.POST['todocaption']
      todo.description=request.POST['tododescription']
      todo.comment=request.POST['todocomment']
      for user_id in request.POST.getlist('forwhom'):
        todo.doers.add(User.objects.get(pk=int(user_id)))
      todo.save()
      return HttpResponseRedirect('/')
  return HttpResponseRedirect('/') # not allowed to edit others' todos


@login_required(login_url="/login/")
def delete(request, todo_id):
  todo = Todo.objects.get(pk=todo_id)
  if todo.author == request.user:
    todo.delete()
  return HttpResponseRedirect('/') # not allowed to delete others' todos