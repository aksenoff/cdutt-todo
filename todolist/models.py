from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    def __unicode__(self):
        return self.caption
    caption = models.CharField(max_length=100)
    pub_date = models.DateTimeField(verbose_name='date published')
    due_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000, blank=True)
    author = models.ForeignKey(User, related_name='todos_by_user')
    doers = models.ManyToManyField(User, related_name='todos_for_user')
    done = models.BooleanField(default=False)

