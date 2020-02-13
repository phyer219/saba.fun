from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Shijing, Ci

def index(request):
    shijing_list = Shijing.objects.all()
    # for v in shijing_list:
    #     v.content = v.content.replace('\n', '<br>') 
    context = {'shijing_list': shijing_list}
    return render(request, 'poetry/index.html', context)

def shijing(request):
    shijing_list = Shijing.objects.all()
    # for v in shijing_list:
    #     v.content = v.content.replace('\n', '<br>') 
    context = {'shijing_list': shijing_list}
    return render(request, 'poetry/shijing.html', context)
def shijing_id(request, shijing_id):
    shijing_list = Shijing.objects.all()
    shijing_id -= 1
    this_shijing = shijing_list[shijing_id]
    # for v in shijing_list:
    #     v.content = v.content.replace('\n', '<br>') 
    context = {'shijing_list': shijing_list, 'shijing_id': shijing_id,
               'this_shijing': this_shijing}
    return render(request, 'poetry/shijing_id.html', context)

def ci(request):
    ci_list = Ci.objects.all()
    # for v in shijing_list:
    #     v.content = v.content.replace('\n', '<br>')
    
    author_list=[]
    aut_id = 0
    aut_list = []
    for aut in ci_list:         # 找出没有重复的作者, 并编号
        if aut.author not in aut_list:
            aut_list.append(aut.author)
            aut_id += 1
            author_list.append({'name': aut.author, 'id': aut_id})
        
    context = {'ci_list': ci_list, 'author_list': author_list}
    return render(request, 'poetry/ci.html', context)

def ci_aut_id(request, ci_aut_id):
    ci_list = Ci.objects.all()
    author_list=[]
    aut_id = 0
    aut_list = []
    for aut in ci_list:         # 找出没有重复的作者, 并编号
        if aut.author not in aut_list:
            aut_list.append(aut.author)
            aut_id += 1
            author_list.append({'name': aut.author, 'id': aut_id})

    ci_aut_id -= 1
    this_aut = aut_list[ci_aut_id]

    ci_this_aut = []
    for ci in ci_list:
        if ci.author==this_aut:
            ci_this_aut.append(ci)
    context = {'this_aut': this_aut, 'ci_this_aut': ci_this_aut}
    return render(request, 'poetry/ci_aut_id.html', context)
