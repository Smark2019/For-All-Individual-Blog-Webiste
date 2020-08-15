from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import Articleform
from django.contrib import messages
from.models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles(request):

    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        context  = {"articles":articles}
        return render(request,"articles.html",context)



    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})


def index (request):
    articles = Article.objects.all()
    return render(request,"index.html",{"articles":articles})
    #return render (request,"index.html")



def about(request):
    return render (request,"about.html")



def detail(request,id):
    
    article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id=id)
    
    comments= article.comments.all()
    context = {"article":article,"comments":comments}

    return render(request,"detail.html",context)





@login_required
def dashboard (request):
    articles = Article.objects.filter(author = request.user)
    context = {"articles" : articles}
    return render(request,"dashboard.html",context)




@login_required
def addarticle(request):
    form = Articleform(request.POST or None,request.FILES or None)
    content = {"form":form}
    if request.method == "POST":
        if form.is_valid():
            article = form.save(commit=False)
            article.author =request.user
            article.save()

            messages.success(request,"Başarılı Şekilde Makaleniz Oluşturuldu")
            return redirect("article:dashboard")
        else:
            messages.warning(request,"BİR ŞEYLER TERS GİTİİ ):")
            return render(request,"addarticle.html",content)
    else:
        
        return render(request,"addarticle.html",content)

@login_required
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form    = Articleform(request.POST or None,request.FILES or None,instance=article)
    content = {"form":form}
    if form.is_valid():
        article = form.save(commit=False)
        article.author =request.user
        article.save()

        messages.success(request,"Başarılı Şekilde Makaleniz Güncellendi ve Kaydedildi.")
        return redirect("article:dashboard")

    return render(request,"update.html",content)

@login_required
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi.")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article,id = id)
    
    if request.method == "POST":
        comment_author  = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment          = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article  = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))

