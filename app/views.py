from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO' : ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)

        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']

            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()

            TDO=Topic.objects.all()
            d1={'TDO':TDO}

            return render(request,'display_topic.html',d1)

        else:
            return HttpResponse ('Invalid Data')
            
    return render (request,'insert_topic.html',d)


def insert_web(request):
    EWFO=WebpageForm()
    d={'EWFO' : EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)

        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']

            TO=Topic.objects.get(topic_name=tn)
            WDO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WDO.save()

            WPDO=Webpage.objects.all()
            d1={'WPDO':WPDO}

            return render (request,'display_web.html',d1)
    return render(request,'insert_web.html',d)

def insert_accessrecord (request):
    EAFO=AccessrecordForm()
    d={'EAFO' : EAFO}

    if request.method=='POST':
        AFDO=AccessrecordForm(request.POST)

        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']

            WO=Webpage.objects.get(pk=n)
            ADO=Accessrecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            ADO.save()

            APDO=Accessrecord.objects.all()
            d1={'APDO' : APDO}
            
            return render (request,'display_accessrecord.html',d1)
    return render (request,'insert_accessrecord.html',d)

