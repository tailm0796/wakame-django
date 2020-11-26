from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lessons
from django.core.exceptions import PermissionDenied
# Create your views here.
class LessonsList(ListView):
    model = Lessons
    template_name = 'LessonsList.html'