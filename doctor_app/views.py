from django.shortcuts import render,redirect
from .models import Doctor

# Create your views here.
def createDoctor(request):
    doctors = Doctor.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        specialist=request.POST.get('specialist')

        doctor=Doctor(name=name,specialist=name)
        doctor.save()
    return render(request,'doctor.html',{"doctors":doctors})

def listdoctor(request):
    doctor=Doctor.objects.all()

    return render(request,'doctorlist.html',{'doctor':doctor})

def detailsview(request,doctor_id):
    doctor=Doctor.objects.get(id=doctor_id)
    return render(request,'detailsview.html',{'doctor':doctor})


def updateview(request,doctor_id):
    doctor=Doctor.objects.get(id=doctor_id)
    if request.method=='POST':
        name = request.POST.get('name')
        specialist = request.POST.get('specialist')

        doctor.name=name
        doctor.specialist=specialist
        doctor.save()
        return redirect("/")
    return render(request,'updateview.html', {'doctor': doctor})
