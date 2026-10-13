from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('detail/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('edit/<slug:slug>/', PostEditeView.as_view(), name='post-edit'),

]