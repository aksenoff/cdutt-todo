from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todolist.views.index'),
    # url(r'^todo/', include('todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^logout/', logout, {'next_page': '/'}),
    url(r'^add/$', 'todolist.views.add'),
    url(r'^add/(?P<user_id>\d+)/', 'todolist.views.add'),
    url(r'^user/(?P<user_id>\d+)/', 'todolist.views.user'),
    url(r'^edit/(?P<todo_id>\d+)/', 'todolist.views.edit'),
    url(r'^delete/(?P<todo_id>\d+)/', 'todolist.views.delete'),
    url(r'^submit/(?P<todo_id>\d+)/', 'todolist.views.submit'),
)
