from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lessons
from django.core.exceptions import PermissionDenied
# Create your views here.
class LessonsList(ListView):
    model = Lessons
    template_name = 'lessons_list.html'
class LessonCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Lessons
    template_name = 'lesson_create.html'
    fields = ('title','body','image')
    login_url = 'login'
    permission_required = 'onlstudy.add_lessons'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class LessonDetail(DetailView):
    model = Lessons
    template_name = 'lesson_detail.html'
class LessonEdit(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Lessons
    template_name = 'lesson_edit.html'
    fields = ('title','body','image')
    login_url = 'login'
    permission_required = 'onlstudy.change_lessons'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class LessonDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Lessons
    template_name = 'lesson_delete.html'
    login_url = 'login'
    permission_required = 'onlstudy.delete_lessons'
    success_url = reverse_lazy('lessions_list')
    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.author != self.request.user:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)