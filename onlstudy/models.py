import uuid
from django.db import models
from django.urls import reverse
# Create your models here.
class Lessons(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])