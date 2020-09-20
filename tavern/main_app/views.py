from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Group
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def landing(request):
    return render(request, 'landing.html')

@login_required
def groups_index(request): 
    return render(request, 'groups/index.html', { 'groups': None })

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('groups_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)