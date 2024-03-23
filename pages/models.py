from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
# Create your models here.
