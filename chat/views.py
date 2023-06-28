from django.shortcuts import render, redirect
from .models import Room, Message, User
from django.http import HttpResponse, JsonResponse
from .utils import name_to_url


def home(request):
    def onunload():
        print('##### Hello from onUnload...')
    
    if request.method == 'POST':
        room_name = request.POST["room_name"].strip()
        username = request.POST["username"].strip()
        if not (len(room_name) and len(username)):
            context = {
                'error': 'The room name and username must be filled out'
            }
            return render(request, 'home.html', context)
        room_to_url = name_to_url(room_name)
        if not Room.objects.filter(url=room_to_url).exists():
            Room.objects.create(name=room_name, url=room_to_url).save()
            room_db = Room.objects.get(url=room_to_url)
            User.objects.create(name=username, room=room_db).save()
            return redirect(f'{room_to_url}/')
        else:
            room_db = Room.objects.get(url=room_to_url)
            if User.objects.filter(name=username, room=room_db.pk).exists():
                context = {
                    'error': 'Username already taken for this room. Try another one.'
                }
                return render(request, 'home.html', context)
            User.objects.create(name=username, room=room_db).save()
            return redirect(f'{room_to_url}/')
    return render(request, 'home.html', {onunload: onunload})


def room(request, room):
    room_db = Room.objects.get(url=room)
    username = User.objects.filter(room=room_db).last()
    context = {
        'username': username.name,
        'room': room_db,
    }
    return render(request, 'room.html', context)


def send(request):
    username = request.POST['username']
    message = request.POST['message'].strip()
    user_db = User.objects.get(name=username)
    Message.objects.create(user=user_db, value=message).save()
    return HttpResponse('Message sent successfully')


def get_messages(request, room):
    room_db = Room.objects.get(url=room)  # Get the current room from the database.
    room_users = User.objects.filter(room=room_db).all()  # Get all users that are in the current room.
    messages = list()
    for user in room_users:  # For each user.
        msg_data_list = Message.objects.filter(user=user).all().values()  # Get all messages from this user.
        if not msg_data_list.__len__():  # If there aren't any messages, skip it.
            continue
        for msg_data in msg_data_list:  # For each message.
            msg_data_dict = {  # Get only the data we need.
                'user': user.name,
                'value': msg_data['value'],
                'timestamp': msg_data['timestamp']
            }
            messages.append(msg_data_dict)  # Add to our message list.
    response = {
        "messages": messages
    }
    return JsonResponse(response)
