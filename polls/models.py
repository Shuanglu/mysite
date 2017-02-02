from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
@python_2_unicode_compatible
class Issue(models.Model):
    issue_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.issue_text

    def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

@python_2_unicode_compatible
class Option(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.option_text


#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)