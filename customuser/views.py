from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            authenticate(
                username=data.get('username'),
                password=data.get('password')
            )
            return HttpResponseRedirect(reverse('main'))
    return render(request, 'form.html', {'form': form})


def logout(request):
    return


# TODO user detail page where you can see current tickets assigned to user,
#      which tickets that user filed, and which tickets that user completed
def user_details(request, user_id):
    return render(request, '', {})



