from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse,HttpResponseRedirect,Http404
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django_request_context import request, g
# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    
    articles = Article.objects.all()
    paginator = Paginator(articles, 5) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request,"articles.html",{"articles":articles})


@login_required(login_url = "user:login")
def dashboard(request):

    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addArticle(request):

    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Article has been created successfully.")
        #return redirect("article:dashboard")
        return HttpResponseRedirect(article.get_absolute_url())
    return render(request,"addarticle.html",{"form":form})
    
def detail(request,id):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article,id = id)

    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url = "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    if request.user == article.author:
        form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
        if  form.is_valid():
            article = form.save(commit=False)
        
            article.author = request.user
            article.save()

            messages.success(request,"Update Succesful!")
            return HttpResponseRedirect(article.get_absolute_url())


        return render(request,"update.html",{"form":form})
    else:
        raise Http404

@login_required(login_url = "user:login")
def deleteArticle(request,id):
    
    article = Article.objects.filter (author = request.user, id = id )

    sup = get_object_or_404(Article, id = id )

    if article:
        
        article.delete()

        messages.success(request,"Article has been deleted successfully.")
        return redirect("article:dashboard")
    elif request.user.is_superuser:
        sup.delete()
        messages.success(request,"Article has been deleted successfully.")
    else:
        raise Http404
    return redirect("article:articles")
@login_required(login_url = "user:login")
def addComment(request,id):
    article = get_object_or_404(Article,id = id)

    
    if request.method == "POST":
        
        comment_author = request.user
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))

@login_required(login_url = "user:login")

def deleteComment(request,id):

    comment = Comment.objects.filter (comment_author = request.user, id = id )

    sup = get_object_or_404(Comment, id = id )

    if comment:
        
        comment.delete()
        messages.success(request,"Comment has been deleted successfully.")
    elif request.user.is_superuser:
        sup.delete()
        messages.success(request,"Comment has been deleted successfully.")
    else:
        raise Http404
    return redirect("article:articles")