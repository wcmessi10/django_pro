from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Board, Reply
from acc.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth  import authenticate
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def index(request):
    pg = request.GET.get("page",1)
    cate = request.GET.get("cate", "")
    kw = request.GET.get("kw", "")

    if kw:#키워드가 있을 때
        if cate == "sub":#카테고리가 sub(제목)일 때
            b = Board.objects.filter(subject__startswith=kw)
            #요청하는 특징을 가진 레코드들을 전부 가져오는 테이블.objects.filter(조건)
        elif cate == "wri":#카테고리가 wri(글쓴이)일 때
            from acc.models import User
            #이 상황에서만 User 가져오는 거라 안에 넣음
            try:

                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()
        elif cate == "sum":#카테고리 sum(내용)
            b = Board.objects.filter(summary__contains=kw)
            #summary__contain=키워드 : 키워드가 포함된 내용
    else:
        b = Board.objects.all()
    pag = Paginator(b,10)
    obj = pag.get_page(pg)
    context ={
        'blist' : obj,
        'cate':cate,
        'kw':kw,
    }
    return render(request,"board/index.html",context)
def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()#자식테이블인 Reply 역참조하기 위해 reply_set사용 
    context = {
        'b' : b,
        'rlist' : r,
    }
    return render(request, "board/detail.html", context)
def delete(request, bpk):
    b = Board.objects.get(id = bpk)
    if b.writer == request.user:
        b.delete()
        messages.error(request,"Board is eliminated!!!")
    else:
        pass
    return redirect("board:index")

def create(request):
    if request.method =="POST":
        sub = request.POST.get("sub")
        con = request.POST.get("con")
        Board(subject=sub, writer=request.user, content=con, pubdate=timezone.now()).save
        return redirect("board:index")        
    return render(request,"board/create.html")

def update(request, bpk):
    b = Board.objects.get(id=bpk)
    #다른 사람이 악의적으로 접근할 때
    if b.writer != request.user:
        return redirect("board:index")
    if request.method =="POST":
        b.subject = request.POST.get("sub")
        b.content = request.POST.get("con")
        b.save()
        return redirect("board:index")
    context = {
        "b" : b,
    }
    return render(request,"board/update.html", context)

def createreply(request, bpk):
    b = Board.objects.get(id=bpk)
    c = request.POST.get("com")
    Reply(b=b, replyer=request.user, comment=c, pubdate=timezone.now()).save()

    return redirect('board:detail', bpk)
def dreply(request,bpk, rpk):
    r = Reply.objects.get(id=rpk)
    if r.replyer == request.user:
        r.delete()
        messages.error(request,"Reply is elininated")
    else:
        pass
    return redirect("board:detail",bpk)

def likey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("board:detail", bpk)

def unlikey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:detail", bpk)
