from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse,HttpResponseRedirect,Http404
from .forms import NewsForm
from .models import News
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


    
def news(request):
    query = request.GET.get("query")

    if query:
        news = News.objects.filter(title__contains = query)
        return render(request,"news.html",{"news":news})
    
    news = News.objects.all()
    paginator = Paginator(news, 10) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request,"news.html",{"news":news})



@login_required(login_url = "user:login")
@permission_required('is_superuser')
def addNews(request):
    form = NewsForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        news = form.save(commit=False)
        
        news.author = request.user
        news.save()

        messages.success(request,"News has been created successfully.")
        #return redirect("news:newsdetail")
        return HttpResponseRedirect(news.get_absolute_url())
    return render(request,"addnews.html",{"form":form})


def newsDetail(request,id):
    #news = News.objects.filter(id = id).first()   
    news = get_object_or_404(News,id = id)
    
    context = {
        "news":news
    }
    
    return render(request,"newsDetail.html",context)

@login_required(login_url = "user:login")
@permission_required('is_superuser')

def updateNews(request,id):

    news = get_object_or_404(News,id = id)
    form = NewsForm(request.POST or None,request.FILES or None,instance = news)
    if form.is_valid():
        news = form.save(commit=False)
        
        news.author = request.user
        news.save()

        messages.success(request,"Update Succesful!")
        return HttpResponseRedirect(news.get_absolute_url())


    return render(request,"newsUpdate.html",{"form":form})
@login_required(login_url = "user:login")
@permission_required('is_superuser')

def deleteNews(request,id):
    news = get_object_or_404(News,id = id)

    news.delete()

    messages.success(request,"News has been deleted successfully.")

    return redirect("news:news")

