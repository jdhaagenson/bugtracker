from django.shortcuts import render
from customuser.models import CustomUser


# Create your views here.
# TODO homepage that shows all tickets, separated by ticket status
#      statuses: New, In Progress, Done, Invalid
def main(request):
    return render(request, '', {})


# TODO filing and creating tickets
def create_ticket(request):
    return render(request, '', {})


# TODO ticket detail page
def ticket_details(request, ticket_id):
    return render(request, '', {})


# TODO edit tickets, limited to only title and description
def edit_ticket(request, ticket_id):
    return render(request, '', {})


# TODO assign a ticket to currently logged in user, which changes status to in progress
def assign_ticket(request, ticket_id):
    return


# TODO mark ticket as invalid
def invalidate(request, ticket_id):
    return


# TODO mark ticket as complete
def complete(request, ticket_id):
    return



