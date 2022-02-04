from django.utils import timezone
from django.shortcuts import redirect, render
from .models import Book
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def index(request):
    b = request.user.book_set.all().order_by('-pubdate')
    context = {
        'blist':b,
    }
    return render(request, 'book/index.html',context)

def delete(request, bpk):
    b = Book.objects.get(id=bpk)
    b.delete()
    messages.error(request,"Bookmark is deleted")
    return redirect('book:index')

def create(request):
    if request.method == "POST":
        t = request.POST.get("title")
        u = request.POST.get("url")
        c = request.POST.get("con")
        i = request.POST.get("impo")
        
        if t and u and c:
            if i:
                imp = True
            else:
                imp = False
            Book(site_name=t, site_url=u, content=c, user=request.user, impo=imp, pubdate=timezone.now()).save()
            messages.success(request,"New Bookmark is created!!!")
            return redirect("book:index")
    return render(request, "book/create.html")