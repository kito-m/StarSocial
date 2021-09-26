from django import template
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns= [
    path('', views.ListGroups.as_view(template_name='groups/group_list.html'), name='all'),
    path('new/', views.GroupCreateView.as_view(), name='create'),
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
]