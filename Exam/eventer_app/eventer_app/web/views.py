from django.shortcuts import render, redirect

from eventer_app.web.forms import CreateProfileForm, CreateEventForm, DeleteEventForm, EditProfileForm, \
    DeleteProfileForm
from eventer_app.web.models import ProfileModel, EventModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'shared/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    events = EventModel.objects.all().order_by('pk')

    context = {
        'events': events,
        'profile': profile,
    }

    return render(request, 'events/dashboard.html', context)


def create_event(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateEventForm()
    else:
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'events/event-create.html', context)


def details_event(request, pk):
    profile = get_profile()
    event = EventModel.objects.filter(pk=pk).get()

    context = {
        'event': event,
        'profile': profile,
    }

    return render(request, 'events/events-details.html', context)


def edit_event(request, pk):
    profile = get_profile()
    event = EventModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CreateEventForm(instance=event)
    else:
        form = CreateEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'event': event,
        'profile': profile,
    }

    return render(request, 'events/event-edit.html', context)


def delete_event(request, pk):
    profile = get_profile()
    event = EventModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteEventForm(instance=event)
    else:
        form = DeleteEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'event': event,
        'profile': profile,
    }

    return render(request, 'events/events-delete.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    events_count = EventModel.objects.all().count()

    context = {
        'user': profile,
        'events_count': events_count,
        'profile': profile,
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)
