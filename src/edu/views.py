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
                              
def pathogen_view(request, pathogen_id=1):
    return render_to_response('pathogen.html',
                              {'pathogen': Pathogen.objects.get(tag=pathogen_id),
                               'iso': Iso.objects.get(pathogen__tag__exact=pathogen_id),
                               'pathtype': PathType.objects.get(pathogen__tag__exact=pathogen_id)}
                             )

def isolation_view(request, isolation_id=1):
    return render_to_response('isolation.html',
                              {'isolation': Iso.objects.get(tag=isolation_id),
                               'ppes': Prevention.objects.filter(iso__tag__exact=isolation_id)}
                             )

def hai_view(request, hai_id=1):
    return render_to_response('hai.html',
                              {'hai': HAI.objects.get(tag=hai_id)}
                             )
                              
def pathtype_view(request, pathtype_id=1):
    return render_to_response('pathtype.html',
                              {'pathtype': PathType.objects.get(tag=pathtype_id)}
                              )

def ppe_view(request, ppe_id=1):
    return render_to_response('ppe.html',
                              {'ppe': Prevention.objects.get(tag=ppe_id)}
                              )
                              