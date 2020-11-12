from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.core.exceptions import PermissionDenied
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class HomePageNews(ListView):
    model = Post
    template_name = 'news.html'
class HomePageNewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
class HomePageNewsCreate(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'news_create.html'
    fields = ('title','imglink','body','recap')
    login_url = 'login'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class HomePageNewsEdit(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'news_edit.html'
    #fields = '__all__'
    fields = ('title','imglink','body','recap')
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class HomePageNewsDelete(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'news_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('news')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)