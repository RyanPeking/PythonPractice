from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse

# Create your views here.

def extremParam(r, name):
    return HttpResponse("My name is {0}".format(name))

def revParse(r):
    return HttpResponse("Your requested URL is {0}".format(reverse('askname')))

def five_get(r):
    return render(r, 'five_get.html')


def five_post(r):
    print(r.POST)
    return render(r, 'one.html')