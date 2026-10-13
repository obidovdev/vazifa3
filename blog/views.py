from django.shortcuts import render
from django.urls import reverse_lazy


from django.views.generic import ListView, DetailView , TemplateView , FormView , CreateView , DeleteView
from .models import Post
from django.views.generic.edit import UpdateView
from .forms import PostCreateForm
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post-list')


class PostEditeView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('post-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'