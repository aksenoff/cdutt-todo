from todolist.models import Todo
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def index(request):
    return HttpResponse("Hello %s" % request.user.username)