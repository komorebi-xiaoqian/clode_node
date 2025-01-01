import time

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from note.models import Note


# Create your views here.
def login_check(a_func):
    def wraspTheFunction(request, *args, **kwargs):
        if 'uname' not in request.session or 'uid' not in request.session:
            return HttpResponseRedirect('/user/login')

        return a_func(request, *args, **kwargs)

    return wraspTheFunction


@login_check
def list_view(request):
    uname = request.session["uname"]
    uid = request.session["uid"]
    notes = Note.objects.filter(user_id=uid, isActivate=True)
    return render(request, 'node/list_node.html', locals())


@login_check
def add_view(request):
    if request.method == "GET":
        return render(request, "node/add_note.html")
    elif request.method == "POST":
        uid = request.session["uid"]
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title or not content:
            return HttpResponse('标题或内容不能为空， <a href="/note/add">返回</a>')
        # if "script" in content:
        try:
            Note.objects.create(title=title, content=content, user_id=uid)
        except:
            return HttpResponse("添加笔记失败， <a href='/note/add'>返回</a>")
        return HttpResponseRedirect(reverse('noteList'))


def mod_view(request, id):
    if request.method == "GET":
        note = Note.objects.get(id=id)
        return render(request, "node/mod_note.html", locals())
    elif request.method == "POST":
        uid = request.session["uid"]
        title = request.POST.get('title')
        content = request.POST.get('content')
        if not title or not content:
            # 使用 reverse 生成修改页面的 URL kwargs={'id': id}
            modify_url = reverse('mod', args=id)
            return HttpResponse(f'标题或内容不能为空,修改失败 <a href="{modify_url}">返回</a>')
        # if "script" in content:
        note = Note.objects.get(id=id)
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect(reverse('noteList'))


def del_view(request, id):
    note = Note.objects.get(id=id)
    note.isActivate = False
    note.save()
    return HttpResponseRedirect(reverse("noteList"))
