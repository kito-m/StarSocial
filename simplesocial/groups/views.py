from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from djangi.urls import reverse
from django.views import generic
from groups.models import GroupMember, Group

class GroupCreateView(LoginRequiredMixin, generic.CreateView):

    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    models = Group

# Create your views here.
