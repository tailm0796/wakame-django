from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
class HomePageNewsCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Post
    template_name = 'news_create.html'
    fields = ('title','body','image')
    login_url = 'login'
    permission_required = 'news.add_post'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class HomePageNewsEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Post
    template_name = 'news_edit.html'
    #fields = '__all__'
    fields = ('title','body','image')
    login_url = 'login'
    permission_required = 'news.change_post'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class HomePageNewsDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Post
    template_name = 'news_delete.html'
    login_url = 'login'
    permission_required = 'news.delete_post'
    success_url = reverse_lazy('news')
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)