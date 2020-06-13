from django import forms
from .models import Article,Comment
from django.views.generic import ListView

class ArticleList(ListView):
    class Meta:
        paginate_by = 2
        model = Article

class ArticleForm(forms.ModelForm):
    
    
    class Meta:
        model = Article
        fields = [
        "title",
        "content",
        "article_image",
        ]

class CommentForm(forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = [
        "comment_content",
        ]
