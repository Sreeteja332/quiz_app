from django.shortcuts import render
from django.http import Http404

# Create your views here.


def starting_page(request):
    try:
        return render(request,"quiz_page/index.html")
    except:
        raise Http404()