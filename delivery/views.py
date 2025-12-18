from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def open_signin(request):
    return render(request, 'signin.html')

def open_signup(request):
    return render(request, 'signup.html')

# def signin(request):
#     #DB's Data
#     user = "gamana"
#     pw = "123"
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if user == username and pw == password:
#             # return HttpResponse(f"Username : {username} password : {password}")
#             return render(request, "success.html") 
#         else:
#             #return HttpResponse(f"Invalid response")
#             return render(request, "fail.html") 
    
#     else:
#         return HttpResponse("Invalid Request")

def signin(request):
    if request.method == 'POST':
        # Fetching data from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Check if a user exists with the provided credentials
            customer = User.objects.get(username=username, password=password)
            return render(request, 'success.html', {'customer': customer})
        except User.DoesNotExist:
            # If credentials are invalid, show a failure page
            return render(request, 'fail.html')
    else:
        return HttpResponse("Invalid Request")
        
    
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        if User.objects.filter(username=username).exists():
            return HttpResponse("This username is already registered. Please use a different email.")
        
        user = User(username=username, password=password, email=email, mobile=mobile, address=address)
        user.save()

        return render(request, "signin.html") 
        # return HttpResponse(f"Username : {username} password : {password} email {email} mobile {mobile} address {address}")
    else:
        return HttpResponse(f"Invalid response, Duplicate User")