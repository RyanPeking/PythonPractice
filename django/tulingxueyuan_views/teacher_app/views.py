from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
from django.views import defaults


def teacher(r):
    return HttpResponse("这是Teacher的一个视图")

def render2_test(request):

    c = dict()
    c["name1"] = "Liudana"
    c["name2"] = "Liuerna"
    c["name3"] = "Liusanna"

    rsp = render(request, "render2.html", context=c)
    return rsp

def render3_test(request):


    from django.template import loader

    # 得到模板
    t = loader.get_template("render2.html")
    print(type(t))

    r = t.render({"name":"Liunana"})
    print(type(r))

    return HttpResponse(r)

def render4_test(request):

    # 反馈回模板render2.html

    rsp = render_to_response("render2.html", context={"name":"Liunana"})

    return rsp

def get404(request):
    return defaults.page_not_found(request, template_name="render2.html")
