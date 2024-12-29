from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.
@login_required
def index(request): 
  return render(request, 'index.html')

# when generate button on index.html is clicked will send url from input here.
@csrf_exempt
def generate_blog(request): 
  if request.method == 'POST': 
    try: 
      data = json.loads(request.body)
      yt_link = data['link']
      return JsonResponse({'content': yt_link})
    except (KeyError, json.JSONDecodeError): 
      return JsonResponse({'error': 'Invalid data sent'}, status = 400)
  # get title of video
  # get transcript
  # use OpenAI to generate the blog
  # save blog to db
  # return blog as reponse
  else: 
    return JsonResponse({'error:': 'Invalid request method'}, status = 405)
  

def user_login(request): 
  if request.method == 'POST': 
    username = request.POST['username']
    password = request.POST['password']

    # Authenticate user
    user = authenticate(request, username = username, password = password)

    # if user exists log in else throw error message
    if user is not None: 
      login(request, user)
      return redirect('/')
    else: 
      error_message = "Invalid username or password"
      return render(request, 'login.html', {'error_message': error_message})
  return render(request, 'login.html')
   
    
def user_logout(request): 
  logout(request)
  return redirect('/')

def user_signup(request): 
  # getting request.body with Python
  if request.method == 'POST': 
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    repeatPassword = request.POST['repeatPassword']

    # password validation check
    if password == repeatPassword: 
      # if passwords match create new user signing up
      try: 
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('/')
      except: 
        error_message = 'Error creating account'
        return render(request, 'signup.html', {'error_message': error_message})
    else: 
      error_message = 'Passwords Do Not Match'
      return render(request, 'signup.html', {'error_message': error_message})

  return render(request, 'signup.html')
