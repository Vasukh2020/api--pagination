from email import message
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    #message='a'
    return render(request, 'home.html')
def login(request):
     if request.method== "POST" :
        # print("request.Post=",request.POST)
        print('dest12')
        name=request.POST['name']
        password=request.POST['password']
        print('name')
        print('password')
        
        user= auth.authenticate(name=name,password=password)
        print('done1')
        #if 1:
        if user is not None:
        #if login(request,user):
        #if User.objects(name=name, password=password).exists():
            print('done2')
            auth.login(request, user)
            i= request.get(user.pk)
            return redirect('home')

            #return render(request,'<i>/detail.html')
        else:
            messages.info(request,'invalid')
            #message='invalid'
            print("it was here ----------------------")
            return HttpResponseRedirect('/home/')
     else:
       print("it wa---------------------")
       return render(request, 'login.html')
def detail(request,pk):
    print("request+++",request)
    obj= LoginUser.objects.get(id=pk)
    context={
        'name':obj.name
    }
    return render(request,"detail.html",context)


 #part of pagination api   
from urllib import response
import requests
from django.core.paginator import Paginator, EmptyPage

def api_list_view(request):

 response=requests.get('https://api.covid19api.com/countries').json()

 r=response
 #print("request::",r)


 page_num= request.GET.get('page')
 

 p =Paginator(response,10)
 print("this is the value of p",p)
 ''''
 try:
      page=p.page(page_num) 
 except EmptyPage:
      page=p.page(page_num) 
      '''
 #print("no of pages:",page_num)
 print("no of pages ",page_num) 

 page=p.page(7) 
 context={
        "response": page
    }
 
 #object_list= response
 print("condext")
 return render (request,"api.html",context)
#copied this to make changes
import json
def api_list_view(request):

 response=requests.get('https://api.covid19api.com/countries').json()

 r=response
 #print("request::",r)
 if 'q' in request.GET:
        print("as it was")
        q=request.GET['q']
        print("searching",q,"+")        

        queryset=request.objects.filter(Country__icontains=q)
        context={
            'object_list':queryset}
        print("it was here")

 else:
  page_num= request.GET.get('page')
 

  p =Paginator(response,10)
  print("this is the value of p",p)
  ''''
  try:
      page=p.page(page_num) 
  except EmptyPage:
      page=p.page(page_num) 
      '''
  #print("no of pages:",page_num)
  print("no of pages ",page_num) 

  page=p.page(7) 
  print("responsw typd os ")
  print(type(response))
  context={
        "response": page,
    }
    
 #list=json.loads(response)
 object_list= response
 print("condext")
 return render (request,"api.html",context)

'''
def api_list_view(request):

 response=requests.get('https://api.covid19api.com/countries').json()

 r=response
 #print("request::",r)


 page_num= request.GET.get('page')
 

 p =Paginator(response,10)
 print("this is the value of p",p)

 try:
      page=p.page(page_num) 
 except EmptyPage:
      page=p.page(page_num) 

 #print("no of pages:",page_num)
 print("no of pages ",page_num) 

 page=p.page(7) 
 print("responsw typd os ")
 print(type(response))
 context={
        "response": page,
    }
    
 #list=json.loads(response)
 object_list= response
 print("condext")
 return render (request,"api.html",context)
'''

def api2_list_view(request):
 print('dasss')
 baseurl='https://rickandmortyapi.com/api/'
 endpoint='character'
 pageNo='/?page=' 
 a=4
 x=str(a)
 print('dasss')

 response = requests.get(baseurl+endpoint+ pageNo+x).json()
 p =Paginator(response,4)
 page_num= request.GET.get('page',1)
 try:
      page=p.page(page_num) 
 except EmptyPage:
      page=p.page(page_num) 
 context={
        "object_list": page
    }
 print("condext",context)
 return render (request,"api2.html",context)    
    
# data=response.json()
#contains all 
 #print("request::",response)

 #print(response)
 #d=data['results'] 
 
# print(d[0]['name'])
 print("it is",response['results'][0]['name'])
 print("asddddddd")

 names= response['results'][0]['name']
 return render (request,"api2.html",names)     

#p=response['info']['pages']
#def getpages(response):
 # return(response['info']['pages'])


'''
def register(request):
    print("it was hereff")
    if request.method== "POST" :
        print("request.Post=",request.POST)
        name=request.POST.get("name")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        print('test344')
        if password2==password1:
             reg = RegisterUser()
             reg.username = request.POST['name']
             print('tetst414')
            #  reg.password(request.POST['password'])
            #  print('tetst4')
            #  reg.save()
            #  print('test12')
            #  #  RegisterUser.objects.create(name = name, password= password1)
            #  #    messages.info(request,'created')
             return render (request, "login.html") 

        else:
           message="invalid"
            # messages.info(request,'invalid') 
    return render (request, "register.html") 
'''
def register(request):
    print("it was hereff")
    if request.method== "POST" :
        print("request.Post=",request.POST)
        name=request.POST['name']
        password1=request.POST['p1']
        password2=request.POST['p2']
        print('test344')
        if password2==password1:
             reg = RegisterUser()
             reg.name = request.POST['name']
             log= LoginUser()
             user=LoginUser.objects.create(name = name, password= password1)
             user.save()
             print('tetst414')
             #  reg.password(request.POST['password'])
             #  print('tetst4')
             #  reg.save()
             #  print('test12')
             #user=RegisterUser.objects.create(name = name, password= password1)
             #user.save()
             #    messages.info(request,'created')
             
             return render (request, "home.html") 

        else:
           message="invalid"
            # messages.info(request,'invalid') 
    return render (request, "register.html") 
