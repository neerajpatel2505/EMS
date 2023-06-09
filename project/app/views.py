from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
from . serializers import *
from rest_framework.renderers import JSONRenderer

# Create your views here.
def homePageView(request):
    return render(request, 'home.html')

def userRegistrationView(request):
    return render(request, 'uregistration.html')

def insertUserDataBase(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        #First we check user is already exist or not
        user=UserDataBase.objects.filter(Email=email)
        if user:
            msg= "User already exist"
            return render(request,'uregistration.html',{'msg':msg})
        else:
            if password == cpassword:
                newuser = UserDataBase.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                msg = "User register Successfully"
                return render(request,'home.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(request,"uregistration.html",{'msg':msg})

def userLoginPage(request):
    return render(request,'ulogin.html')

def uLogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=UserDataBase.objects.get(Email=email)
        if user:
            if user.Password==password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request,'userdashboard.html')
        else:
            msg="Invalid Email or Password"
            return render(request,'ulogin.html',{'msg':msg})
    else:
        msg="user dose not exit"
        return render(request,'uregistration.html',{'msg':msg})
#==================================================================================================
def adminRegistrationView(request):
    return render(request,'aregistration.html')

def insertAdminDataBase(request):
    if request.method=='POST':
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        contact=request.POST["contact"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        
        #First we check user is already exist or not
        user=AdminDataBase.objects.filter(Email=email)
        if user:
            msg= "User already exist"
            return render(request,'aregistration.html',{'msg':msg})
        else:
            if password == cpassword:
                newuser = AdminDataBase.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                msg = "User register Successfully"
                return render(request,'home.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(request,"aregistration.html",{'msg':msg})

def adminLoginPage(request):
    return render(request,'alogin.html')

def aLogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        newuser=AdminDataBase.objects.get(Email=email)
        if newuser:
            if newuser.Password==password:
                request.session['Firstname']=newuser.Firstname
                request.session['Lastname']=newuser.Lastname
                request.session['Email']=newuser.Email
                return render(request,'admindashboard.html')
        else:
            msg="Invalid Email or Password"
            return render(request,'alogin.html',{'msg':msg})
    else:
        msg="user dose not exit"
        return render(request,'sregistration.html',{'msg':msg})
#===========================================================================================
def enquiryView(request):
    return render(request,'enquiry.html')

def insertEnquiryDataBase(request):
    if request.method=='POST':
        sname=request.POST["sname"]
        email=request.POST["email"]
        contact=request.POST["contact"]
        enquiry=request.POST["enquiry"]
        user = EnquiryDataBase.objects.create(Studentname=sname,Email=email,Contact=contact,Enquiry=enquiry)
        msg= "Enquiry Successfully"
        return redirect('home')
#===============================(CRUD)==========================================

def showPage(request):
    all_data=EnquiryDataBase.objects.all()
    return render(request,'showpage.html',{'key1':all_data})

#Edit page view
def EditPage(request,pk):
    #fetching the data of perticular ID
    get_data=EnquiryDataBase.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})

#Update data View
def UpdateData(request,pk):
    udata=EnquiryDataBase.objects.get(id=pk)
    udata.Studentname=request.POST['studentname']
    udata.Enquiry=request.POST['enquiry']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    #Query for update
    udata.save()
    return redirect('showpage')

#Delete data View
def DeleteData(request,pk):
    ddata=EnquiryDataBase.objects.get(id=pk)
    #Query for delete
    ddata.delete()
    return redirect('showpage')

#==========================API=====================================================
def user_details_pk(request,pk=None):
    user=UserDataBase.objects.get(id=pk)
    serializer=UserDataBaseSerializer(user)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)
def user_details_list(request):
    user=UserDataBase.objects.all()
    serializer=UserDataBaseSerializer(user,many=True)
    #json_data= JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

def admin_details_pk(request,pk=None):
    admin=AdminDataBase.objects.get(id=pk)
    serializer=AdminDataBaseSerializer(admin)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)
def admin_details_list(request):
    admin=AdminDataBase.objects.all()
    serializer=AdminDataBaseSerializer(admin,many=True)
    #json_data= JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

def enquiry_details_pk(request,pk=None):
    enquiry=EnquiryDataBase.objects.get(id=pk)
    serializer=EnquiryDataBaseSerializer(enquiry)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)
def enquiry_details_list(request):
    enquiry=EnquiryDataBase.objects.all()
    serializer=EnquiryDataBaseSerializer(enquiry,many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data,safe=False)