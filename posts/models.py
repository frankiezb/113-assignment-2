from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):                       #inheritance
    title = models.CharField(max_length=128)    #composition
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absoulute_url(self):
        return reverse("detail", args=[self.id])