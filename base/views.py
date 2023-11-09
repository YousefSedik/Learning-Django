from django.shortcuts import render, redirect
from .models import Room, Topic, Message
from .forms import RoomForm 
from django.db.models import Q 
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages 

# Create your views here.
rooms = [{"name":"frontend", "id":1}, {"name":"backend", "id":2},{"name":"AI", "id":3}]


def loginPage(re):
    context = {} 
    
    if re.method == 'POST':
        
        username = re.POST.get('username') 
        password = re.POST.get('password')
        print(username, password)
        try:
            user = User.objects.get(username= username)
        except:
            messages.error(re, "user doesn't exist")
            
    return render(re, 'base/login_register.html', context)

def Home(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(Q(topic__name__contains=q) |
                                Q(name__icontains=q) |
                                Q(description__icontains = q)
                                ) 

    context = {'data': rooms}        
    topics = Topic.objects.all()
    room_count = rooms.count()
    context['room_count'] = room_count
    context['topics'] = topics
    return render(request, 'base/home.html', context)

def room(re):
    return render(re, 'base/room.html')

def RoomSpeci(re, pk):
    rooms = Room.objects.all()
    
    room = None 
    for i in rooms:
        if i['id'] == int(pk):
            room = i 
    context = {'room': room}
    return render(re, 'base/room.html', context)


def createRoom(re):
    form = RoomForm()
    if re.method == "POST":
        form = RoomForm(re.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        
        else:
            print("Whyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    context = {'form':form}
    return render(re, 'base/room_form.html', context)

def updateRoom(re, pk):
    
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if re.method == 'POST':
        form = RoomForm(re.POST, instance=room) 
        if form.is_valid():
            form.save() 
            return redirect('Home')
    return render(re, "base/room_form.html", {'form':form})
    
    
    
def deleteRoom(re, pk):
    room = Room.objects.get(id=pk)
    if re.method == 'POST':
        room.delete()
        return redirect('Home')
    return render(re, 'base/delete.html', {'obj':room })