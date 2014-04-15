from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse
from .models import Article, Pathogen, Iso, Prevention, PathType, HAI


def home_page(request):
    return render_to_response('home.html',
                              {'pathogens': Pathogen.objects.all(),
                               'isolations': Iso.objects.all(),
                               'pathtypes': PathType.objects.all(),
                               'hais': HAI.objects.all(),
                               'ppes': Prevention.objects.all()
                               }, )
#def front_page(request):
 #   return render_to_response('home.html',
 #                             {'articles': Iso.objects.filter(iso_type__tags__exact='contactplus')
#
 #                              }, )

def article_view(request, article_id=1):
    return render_to_response('article.html',
                              {'article': Article.objects.get(id=article_id)}
                             )
                              
def pathogen_view(request, slug):
    return render_to_response('pathogen.html',
                              {'pathogen': Pathogen.objects.get(slug=slug),
                               'iso': Iso.objects.get(pathogen__slug__exact=slug),
                               'pathtype': PathType.objects.get(pathogen__slug__exact=slug)}
                             )

def isolation_view(request, slug):
    return render_to_response('isolation.html',
                              {'isolation': Iso.objects.get(slug=slug),
                               'ppes': Prevention.objects.filter(iso__slug__exact=slug)}
                             )

def hai_view(request, slug):
    return render_to_response('hai.html',
                              {'hai': HAI.objects.get(slug=slug)}
                             )
                              
def pathtype_view(request, slug):
    return render_to_response('pathtype.html',
                              {'pathtype': PathType.objects.get(slug=slug)}
                              )

def ppe_view(request, slug):
    return render_to_response('ppe.html',
                              {'ppe': Prevention.objects.get(slug=slug)}
                              )
                              