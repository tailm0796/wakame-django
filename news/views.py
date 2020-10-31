from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class HomePageNews(ListView):
    model = Post
    template_name = 'news.html'
class HomePageNewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
class HomePageNewsCreate(CreateView):
    model = Post
    template_name = 'news_create.html'
    fields = '__all__'
class HomePageNewsEdit(UpdateView):
    model = Post
    template_name = 'news_edit.html'
    fields = '__all__'
class HomePageNewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')