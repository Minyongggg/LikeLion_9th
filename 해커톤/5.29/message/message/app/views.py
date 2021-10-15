from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Chatroom, Chat, Person
from django.contrib import admin, auth
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if (request.method == 'POST'):
        find_user = User.objects.filter(username=request.POST['username'])
        if (find_user):
            error = '중복되는 아이디입니다.'
            return render(request, 'registration/signup.html', {'error': error})

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
        )
        auth.login(request, new_user)
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method == 'POST'):
        login_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if (login_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다.'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(request, login_user)
        return redirect('home')

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)

    return redirect('home')


def chatlist(request):
    friends = User.objects.all().exclude(username=request.user.username).exclude(username='admin')

    return render(request, 'chatlist.html', {'friends': friends})

def makeroom(request, friend_pk):
    find_room = Chatroom.objects.filter(chatter1 = request.user).filter(chatter2 = User.objects.get(pk=friend_pk))
    if not (find_room):
        find_room = Chatroom.objects.filter(chatter2 = request.user).filter(chatter1 = User.objects.get(pk=friend_pk))
    
    if not (find_room):
        new_room = Chatroom.objects.create(
            chatter1 = request.user,#User.objects.get(pk=request.user),
            chatter2 = User.objects.get(pk=friend_pk)
        )
        return redirect('chatroom', new_room.pk, friend_pk)
        #return render(request, 'chatroom.html', {'chatroom': new_room})
    
    return redirect('chatroom', find_room[0].pk, friend_pk)
    #return render(request, 'chatroom.html', {'chatroom': find_room[0]})

def chatroom(request, room_pk, friend_pk):
    room = Chatroom.objects.get(pk=room_pk)
    chats = Chat.objects.filter(room=room).order_by('time')
    friend = User.objects.get(pk=friend_pk)
    chats.filter(From=friend).filter(read=False).update(
        read=True
    )


    if (request.method=='POST'):
        new_chat = Chat.objects.create(
            From = request.user,
            To = User.objects.get(pk=friend_pk),
            content = request.POST['content'],
            time = datetime.datetime.today(),
            room = room
        )
        return redirect('chatroom', room_pk, friend_pk)

    return render(request, 'chatroom.html', {'room': room, 'chats': chats, 'friend': friend})


