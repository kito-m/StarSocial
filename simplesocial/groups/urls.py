from django import template
from django.urls import path
from . import views
urlpatterns= [
    path('', views.ListGroups.as_view(template_name='groups/group_list.html'), name='all'),
    path('new/', views.GroupCreateView.as_view(), name='create'),
    path('posts/<slug>/', views.SingleGroup.as_view(), name='single'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave')
]