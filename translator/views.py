from django.shortcuts import redirect, render
import googletrans
from googletrans import Translator

def index(request):
    #src : 출발지 dest : 목적지
    context = {#context를 통해 모든 googletrans.Languages를 불러모으기
        "ndict" : googletrans.LANGUAGES
    }
    if request.method == "POST":
        before = request.POST.get("before")
        belang = request.POST.get("belang")
        aflang = request.POST.get("aflang")
        translator = Translator() 
        print(before, belang, aflang)
        a = translator.translate(before, src=belang, dest=aflang)
        context.update({#context에 if문으로 추가 내용넣으려면 .update({})를 해주면 된다.
            'a' : a.text,
            'before' : before,
            'belang' : belang,
            'aflang' : aflang,
        })
        return render(request,"translator/index.html", context)
    return render(request,"translator/index.html", context)

