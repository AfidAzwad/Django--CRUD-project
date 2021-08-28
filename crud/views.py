from django.core.checks import messages
from django.shortcuts import redirect, render
from django.utils.html import format_html
from crud import forms
from crud.models import Students
# Create your views here.

def home(request):
    userlist = Students.objects.order_by('name')
    diction = {'title':"Home", 'users': userlist}
    return render(request, 'crud/index.html', context=diction)

def userform(request):
    form = forms.Userform()

    if request.method == "POST":
        email = request.POST.get('email')
        if Students.objects.filter(email=email).exists():
            diction = {'exist': "email is already exists"}
            return render(request, 'crud/studentvalidation.html', context=diction)
        else:
          form = forms.Userform(request.POST)
          if form.is_valid():
            form.save(commit=True)
            return home(request)

    diction = {'title':"User Form", "userform": form}
    return render(request, 'crud/studentform.html', context=diction)


def userprofile(request,userid):
    userinfo = Students.objects.get(pk=userid)
    diction = {'title':"Userprofile", 'userinfo': userinfo}
    return render(request, 'crud/student.html', context=diction)


def userupdate(request,userid):
    userinfo = Students.objects.get(pk=userid)
    form = forms.Userform(instance= userinfo)

    if request.method == "POST":
         form = forms.Userform(request.POST, instance=userinfo)

         if form.is_valid():
             form.save(commit=True)
             return home(request)

    diction = {'title':"Update", 'userinfo': form}
    return render(request, 'crud/studentupdate.html', context=diction)



def userdelete(request,userid):
    userinfo = Students.objects.get(pk=userid).delete()
    diction = {'title':"Userdelete", 'delete_mss': "Delete Done"}
    return render(request, 'crud/studentdelete.html', context=diction)

