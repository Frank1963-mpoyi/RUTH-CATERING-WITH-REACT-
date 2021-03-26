from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import Song 







def login_(request):
    print(request)
    if request.method   == "POST":
    
        username      = request.POST.get("uname")
        password      = request.POST.get("pass")
        user = authenticate(username=username, password=password)# the field in yellow are from database
        login(request, user) 
        return redirect("/")
        
    context         =  {}
    template_name   = 'blog/login.html'
    return render(request, template_name, context)




def signup(request, *args, **kwargs):
    #print(request)
    
    if request.method   == "POST" :
        email_1 = request.POST.get("email")
        #print(Email)
        username_1      = request.POST.get("usernam")
        first_name_1    = request.POST.get("fname")
        last_name_1     = request.POST.get("lname")
        password_1      = request.POST.get("pass1")
        password_2      = request.POST.get("pass2")
        
        # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        myuser = User.objects.create_user(username_1, email_1, password_1)
        # At this point, myuser is a User object that has already been saved
        
        #myuser.first_name /object plus field name 
        # to the database. You can continue to change its attributes
        # if you want to change other fields
        myuser.first_name   = first_name_1 
        myuser.last_name    = last_name_1
        myuser.save()
        
        # if the credentials match login this user
        # user = authenticate(username=username_1, password=password_1)# the field in yellow are from database
        # login(request, user) 
        return redirect(login_)
    context = {}
    template_name = 'blog/signup.html'
    return render(request, template_name, context)

















#========    to solve ===============
# handle validation for : UNIQUE constraint failed: auth_user.username
# the user register the existant credential 

        # my own method to avoid error if the list is empty 
        # list1 = [email_1, username_1, first_name_1, last_name_1,  password_1, password_2 ]
        # if list1 == None :
        #     print("Enter a value ")
    
        


