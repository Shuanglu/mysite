from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=3000, blank=True)
    pub_date = models.DateTimeField()
    def __str__(self):
        return self.title


@python_2_unicode_compatible
class BlogDetail(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.CharField(max_length=3000)
    num = models.IntegerField(default=0)
    title = models.TextField(default='HelloWorld')
    def __str__(self):
        return self.title
