from django.shortcuts import render,HttpResponse
from datetime import datetime
from dev.models import contact

# Create your views here.
def index(request):
    context = {
        "variable 1":"this is good",
        "variable 2":"that is gpo"
    }
    return render(request,'ind3x.html',context)
    # return HttpResponse('this is homepage')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('this is about page')

def services(request):
    return render(request,'services.html')
    # return HttpResponse('this is service page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = contact(name = name,email = email,phone = phone,desc = desc,date = datetime.today())
        contacts.save()

    return render(request,'contact.html')
    # return HttpResponse('this is contact page')