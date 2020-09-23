
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Group, Profile, System
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from random import choice
from .forms import ExtendedUserCreationForm, GroupForm


def landing(request):
    return render(request, 'landing.html')


@login_required
def groups_index(request):
    if hasattr(request.user, 'profile'):
        groups = Group.objects.filter(
            players=request.user.profile.id).order_by('date')
        return render(request, 'groups/index.html', {'groups': groups})
    else:
        return redirect('profile_form')


@login_required
def groups_detail(request, group_id):
    return redirect('groups_index') # TODO


@login_required
def lfg(request):
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
        groups = Group.objects.filter(
            looking=True, system__in=profile.systems.all())
        groups = groups.exclude(players=profile.id).exclude(contenders=profile.id)
        if groups.count() > 0:
            group = choice(groups)
        else:
            group = None
        return render(request, 'groups/lfg.html', {'group': group})
    else:
        return redirect('profile_form')


@login_required
def add_contender(request):
    if hasattr(request.user, 'profile'):
        group = Group.objects.get(id=request.POST['group_id'])
        group.contenders.add(request.user.profile.id)
        return redirect('lfg')
    else:
        return redirect('profile_form')


class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['group_name', 'system', 'date', 'location', 'details']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            form = GroupForm(request.POST)
            if form.is_valid():
                new_group = form.save()
                new_group.players.add(request.user.profile.id)
            # TODO: un-stub when we have single group view
            return redirect('groups_index')
        else:
            return redirect('profile_form')


@login_required
def profile(request):
    if hasattr(request.user, 'profile'):
        profile = Profile.objects.get(user=request.user)
        return render(request, 'main_app/profile.html', {'profile': profile})
    else:
        return redirect('profile_form')


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['systems', 'date', 'location', 'bio', 'avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['systems', 'date', 'location', 'bio', 'avatar'] 


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('profile_form')
        else:
            error_message = 'Invalid sign up - try again'
    form = ExtendedUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
