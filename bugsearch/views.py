from django.http import HttpResponse,Http404
from django.shortcuts import render
from django.utils import timezone
from .models import IP
from lib.bugcrawl import *
from urllib import quote

def index(request, page=1):
    retCrawl = BuTian(page).butianBugpage()
    if int(page) <= 0:
        page = 1
    return render(request, 'index.html', {"context": retCrawl, "tag":"bugsearch/page/", "pages": {"previous": int(page)-1, "next": int(page)+1}})

def search(request, keyword, page=1):
    retCrawl = BuTian(page).butianSearch(quote(keyword.encode("utf-8")))
    if int(page) <= 0:
        page = 1
    return render(request, 'index.html', {"context": retCrawl, "tag": u"bugsearch/search/{}/page/".format(keyword), "pages": {"previous": int(page)-1, "next": int(page) + 1}})

