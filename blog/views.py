from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Person
from .forms import MoveForm
from django.utils import timezone


def home(request):
    rooms = Room.objects.all()
    persons = Person.objects.all()
    print("La page affichée utilise la fonction home.")
    return render(request, 'blog/home.html', {'rooms': rooms, 'persons': persons})


def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    persons = room.getPersons()
    return render(request, 'blog/room_detail.html', {'room': room, 'persons': persons})


def person_detail(request, pk, message="", error=False):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        # old location buffering
        old_location = get_object_or_404(Room, pk=person.location.pk)
        form = MoveForm(request.POST, instance=person)
        if form.is_valid():
            form.save(commit=False)
            # checking if new location is available
            new_location = get_object_or_404(Room, pk=person.location.pk)
            if new_location.available:
                # user update
                form.save(commit=True)
                # old location update
                old_location.updateAvailability()
                old_location.save()
                # new location update
                new_location.updateAvailability()
                new_location.save()
                # return redirect('person_detail', pk=pk)
                person.updatePlanet()
                message = "Le changement a correctement été effectué."
            else:
                message = "Le lieu " + new_location.name + " n'est pas libre."
                error = True
                person = get_object_or_404(Person, pk=pk)
                # return redirect('person_detail', pk=pk)
        else:
            message = "La valeur entrée dans le formulaire n'est pas valide."
            error = True
            person = get_object_or_404(Person, pk=pk)
            # return redirect('person_detail', pk=pk)
    else:
        form = MoveForm()
    return render(request,
                  'blog/person_detail.html',
                  {'person': person, 'form': form, 'message': message, "warning": error})


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'blog/person_list.html', {'persons': persons})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'blog/room_list.html', {'rooms': rooms})
