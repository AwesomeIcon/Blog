from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import Tag, Article, Author

def index(request, page_num = 1):
	posts = list(Article.objects.all())
	paginator = Paginator(posts, 2)
	t = loader.get_template("index.html")
	c = Context({'posts':paginator.page(int(page_num))})
	return HttpResponse(t.render(c))
