from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def login_view(request):
    return render(request, '', {})


def logout(request):
    return


# TODO user detail page where you can see current tickets assigned to user,
#      which tickets that user filed, and which tickets that user completed
def user_details(request, user_id):
    return render(request, '', {})




