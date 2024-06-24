from django.shortcuts import render,redirect
from rooftop.forms import sage
from rooftop.forms import reserve
from rooftop.forms import comment


# Create your views here.
def home(request):
     if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']
        print(name,email,phone,date,time,message)
        obj=reserve()
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.date=date
        obj.time=time
        obj.message=message
        obj.save()

     context={

    }
     return render(request,'home.html',context)
    

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')
 
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name,email,phone,message)
        obj=sage()
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.message=message
        obj.save()

    context={

    }
    return render(request,'contact.html',context)

def gallery(request):
    return render(request,'gallery.html')

def review(request):
   feedback=comment.objects.all()
   
   if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name,email,subject,message)
        obj=comment()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()

   context={
       'reviews': feedback 
   }
   #return redirect ('allreview.html')
   return render(request,'review.html',context)
    
#def allreview(request):
     #   feedback=comment.objects.all()
      #  return render(request,'review.html',{'reviews':feedback})