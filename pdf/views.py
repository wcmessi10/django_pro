from django.shortcuts import render
import pdfplumber

# Create your views here.
def index(request):
    if request.method == "POST":
        p = request.FILES.get("pdf")
        pdf = pdfplumber.open(p)
        text = "" # 각 페이지 총합해서 변환하기 위해
        for i in range(len(pdf.pages)):
            fpage = pdf.pages[i]
            text += fpage.extract_text()
        pdf.close()
        context = {
            'text':text,
        }
        return render(request, 'pdf/index.html',context)

    return render(request, 'pdf/index.html')