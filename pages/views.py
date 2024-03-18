from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contacts
from comments.models import Publish
from comments.forms import DocumentForm

# Create your views here.

def index(request):
    return render(request,'pages/index.html')


def about(request):
    return render(request,'pages/about.html')

def studies(request):
    return render(request,'pages/studies.html')

def contact(request):
    sugg = None
    email = None
    if request.method == 'POST' and 'sub' in request.POST:
        if 'ta' in request.POST: sugg = request.POST['ta']
        else: messages.error(request,'قم بادخال مقترحك ')
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'قم بادخال إيميلك ')

        if sugg and email:
            contact = Contacts()
            contact.suggestion = sugg
            contact.email = email
            contact.save()
            messages.success(request, 'تم اضافة مقترحك')
            return render(request,'pages/contact.html')
        else:
            messages.error(request, 'تحقق من وجود حقول فارغة')
    return render(request,'pages/contact.html')

def patrols(request):
    return render(request,'pages/patrols.html')

def news(request):
    return render(request,'pages/news.html')

def showDetailStudies(request):
    publish = None
    file_up = None
    type = None
    
    if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            if 'type' in request.POST: type = request.POST['type']
            file_up = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid():

                if  publish and file_up and type:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.type = type
                    new_publish.save()
                    messages.success(request, 'تم إضافة المنشور بنجاح')
                    return render(request,'pages/showDetailStudies.html')
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                    return render(request,'pages/showDetailStudies.html')
            else:
                messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'pages/showDetailStudies.html')
        
    else:
        return render(request,'pages/showDetailStudies.html')
    
    # return render(request,'pages/showDetailStudies.html')

def showDetailPatrols(request):
   publish = None
   file_up = None
   type = None
    
   if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            if 'type' in request.POST: type = request.POST['type']
            file_up = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid():

                if  publish and file_up and type:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.type = type
                    new_publish.save()
                    messages.success(request, 'تم إضافة المنشور بنجاح')
                    return render(request,'pages/showDetailPatrols.html')
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                    return render(request,'pages/showDetailPatrols.html')
            else:
                messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'pages/showDetailPatrols.html')
        
   else:
        return render(request,'pages/showDetailPatrols.html')

def showDetailNews(request):
   publish = None
   file_up = None
   type = None
    
   if request.method == 'POST' and 'send' in request.POST:
        if request.user.is_authenticated:
            if 'publish' in request.POST: publish = request.POST['publish']
            if 'type' in request.POST: type = request.POST['type']
            file_up = DocumentForm(request.POST, request.FILES)
            if file_up.is_valid():

                if  publish and file_up and type:
                    new_publish = Publish()
                    new_publish.post = publish
                    new_publish.user_id = request.user
                    if request.user.is_superuser == True:
                        new_publish.is_allowed = True
                    else:
                        new_publish.is_allowed = False
                    new_publish.file = request.FILES['docfile']
                    new_publish.type = type
                    new_publish.save()
                    messages.success(request, 'تم إضافة المنشور بنجاح')
                    return render(request,'pages/showDetailNews.html')
                else:
                    messages.error(request, 'تحقق من وجود حقل فارغة')
                    return render(request,'pages/showDetailNews.html')
            else:
                messages.error(request, 'تحقق من وجود حقل فارغة')
                return render(request,'pages/showDetailNews.html')
        
   else:
        return render(request,'pages/showDetailNews.html')

   

