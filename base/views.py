from django.shortcuts import render, redirect
from .models import Room, Topic, Message
from .forms import RoomForm 


# Create your views here.
rooms = [{"name":"frontend", "id":1}, {"name":"backend", "id":2},{"name":"AI", "id":3}]

def Home(request):
    
    rooms = Room.objects.all()
    context = {'data': rooms}    
    topics = Topic.objects.all()
    context['topics'] = topics
    return render(request, 'base/home.html', context)

def room(re):
    rooms = Room.objects.all()
    context = {'room': rooms}
    return render(re, 'base/room.html', context)

def RoomSpeci(re, pk):
    
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