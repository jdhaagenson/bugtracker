from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, logout, login
from customuser.models import CustomUser
from bugtrack.models import Ticket
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # breakpoint()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=username,
                password=password
            )
            # breakpoint()
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('main')))
    form = LoginForm()
    return render(request, 'form.html', {'form': form, 'page': 'Login to BugTracker🐞'})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


@login_required
def user_details(request, userid):
    user = CustomUser.objects.get(id=userid)
    assigned = Ticket.objects.filter(assigned_to=user)
    completed = Ticket.objects.filter(completed_by=user)
    created = Ticket.objects.filter(created_by=user)
    return render(request, 'profile.html',
                  {'user': user, 'assigned': assigned, 'completed': completed, 'created': created})



