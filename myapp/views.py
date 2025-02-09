from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Province 
# Create your views here.

def index(request):
    return render(request,"index.html")

def model(request):
    return render(request,"model.html")  

# def province_list(request):
#     provinces = Province.objects.all().order_by('name')  # ดึงข้อมูลจังหวัดทั้งหมดและเรียงตามชื่อ
#     return render(request, "province.html", {"provinces": provinces})    