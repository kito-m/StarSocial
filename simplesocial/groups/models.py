from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.urls import reverse

# Groups models.py
# Create your models here.

import misaka

from django.contrib.auth import get_user_model

User = get_user_model()

from django import template
register = template.Library()

class Group(Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, blank=True, default='', )
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slugs': self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(Model):
    group = models.ForeignKey(Group, related_name='membership', on_delete=CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group', 'user')
    
