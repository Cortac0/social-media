from django.shortcuts import render, redirect

from .models import User

def index(request):
    all_users = User.objects.all()

    for u in all_users:
        u.post_list = u.posts.all()

    return render(request, "user/index.html", context={
        'users': all_users
    })

def new_user(request):
    return render(request, "user/new.html")

def create(request):
    new_user = User(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
    )
    new_user.save()

    return redirect("/user")
