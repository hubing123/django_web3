from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Article
# Create your views here.


def article_detail(request,article_id):
    # try:
    #     article=Article.objects.get(id=article_id)
    #     context={}
    #     context['article_obj']=article
    #     # return render(request,"article_detail.html",context)
    #     return render_to_response("article_detail.html",context)
    # except Article.DoesNotExist:
    #     raise Http404("not exist")
    # # return HttpResponse("<h2>文章标题是：%s </h2><br> 文章内容是: %s" % (article.title,article.content))
    article=get_object_or_404(Article,pk=article_id)
    context={}
    context['article_obj']=article
    return render_to_response("article_detail.html",context)

def articles_list(request):
    articles=Article.objects.all()
    context={}
    context['articles']=articles
    return render_to_response("articles_list.html",context)