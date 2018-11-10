from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indexPageView(request):
    simple_message_dict = {'check_message':'Hello From the views.py file'}
    return render(request,"appone/basic.html",context=simple_message_dict)