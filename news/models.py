from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class News(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.PROTECT) 
    title = models.CharField(max_length = 70)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    news_image = models.ImageField(blank = True,null = True)

    def __str__(self):
        return self.title
    def  get_absolute_url(self):
        return reverse('news:newsDetail', kwargs={'id': self.id})

    class Meta:
        ordering = ['-created_date']
