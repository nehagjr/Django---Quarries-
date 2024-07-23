from django.shortcuts import render
from django.http import HttpResponse
from .models import Student 
# Create your views here.
def index(request):
    # d=Student.objects.all()
    # d=Student.objects.all().first()
    # d=Student.objects.all().last()
    # d=Student.objects.filter(Student_nm="Neha Patel")
    # d=Student.objects.order_by('Student_nm')
    # d=Student.objects.order_by('-Student_nm')
    # d=Student.objects.order_by('Student_nm').reverse()
    # d=Student.objects.order_by('?')
    # d=Student.objects.exclude(Student_nm="Neha Patel")

    # d=Student.objects.values('Student_nm')

    # print(d)
    # print(d.values())

    #---------------------single object return------------------


    #---------------get method used only with primery key column------------ 
    # d=Student.objects.get(id=2)
    # d=Student.objects.get(Student_nm='Om') #it through error
    # d=Student.objects.first()

    # d=Student.objects.order_by('Student_nm').first() #ascending order
    # d=Student.objects.order_by('-Student_nm').first() #desending order

    # d=Student.objects.order_by('Student_nm').last()

    # d=Student.objects.latest('id')

    # d=Student.objects.create(Student_nm="Pawan Patel",email="pawan.gmail.com",city='gujrat',dep_nm='ML')

    d=Student.objects.get_or_create(Student_nm="Pawan Patel",email="pawan.gmail.com",city='gujrat',dep_nm='ML')

    print(d)
    return HttpResponse(d)






    return HttpResponse("hiiiiiiiiiiiiiiii")