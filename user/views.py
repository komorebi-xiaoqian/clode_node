from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from user.models import User


def login_view(request):
    if request.method == "GET":
        if "uname" in request.session and "uid" in request.session:
            return HttpResponse(f"欢迎{request.session['uname']},"
                                f"请访问其他功能或者<a href='/user/logout/'>退出登录</a>")

        return render(request, "user/login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        if not username or not password:
            return HttpResponse("用户名或密码不能为空")
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("用户名或密码错误")
        if user.password != password:
            return HttpResponse("用户名或密码错误")

        # 保持登录状态
        request.session['uname'] = user.username
        request.session['uid'] = user.id
        # user = User.objects.filter(username=username)
        # if not user:
        #     return HttpResponse("该用户不存在，请注册用户")
        # else:
        #     if password != user.password:
        #         return HttpResponse("密码输入错误")
        return HttpResponseRedirect(reverse('noteList'))


def reg_view(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        password_two = request.POST.get("password_two")
        if not username or not password or not password_two:
            return HttpResponse("用户名或密码不能为空")
        if User.objects.filter(username=username):
            return HttpResponse("用户名太受欢迎，换一个试试")
        if password != password_two:
            return HttpResponse("两次密码不一致")
        user = User.objects.create(username=username, password=password)

        return HttpResponse("创建用户成功")


def logout_view(request):
    if "uname" not in request.session or "uid" not in request.session:
        return HttpResponse("您还没有登录")
    del request.session['uid']
    del request.session['uname']
    return HttpResponse("注销成功")

