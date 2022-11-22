from django.shortcuts import render
from django.http import HttpResponse # first set import 

# Create your views here.

def aboutme(request):
    return render(request,'aboutme.html') 



def contact(request):
    return render(request,'contact.html') 


def education(request):
    return render(request,'education.html') 


def footer(request):
    return render(request,'footer.html') 


def portfolio(request):
    return render(request,'portfolio.html') 


def skill(request):
    return render(request,'skill.html') 


def workexp(request):
    return render(request,'workexp.html') 






