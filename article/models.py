from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(blank = True,null = True)
    def __str__(self):
        return self.title
    def  get_absolute_url(self):
        return reverse('article:detail', kwargs={'id': self.id})

    class Meta:
        ordering = ['-created_date']

    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length = 50)
    comment_content = models.CharField(max_length = 200)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content


    class Meta:
        ordering = ['-comment_date']

    