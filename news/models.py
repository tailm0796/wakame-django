from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    imglink = models.CharField(max_length=200)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    body = models.TextField()
    recap = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('news_detail',args=[str(self.id)])
    def save(self, *args, **kwargs):
        super().save()