# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
import logging


logger = logging.getLogger(__name__)

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        print(request.POST['csrfmiddlewaretoken'])
    return render(request, "post.html", ctx)