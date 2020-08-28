from django.shortcuts import render
from customuser.models import CustomUser
from bugtrack.models import Ticket
from django.shortcuts import HttpResponseRedirect, reverse


# Create your views here.
# TODO homepage that shows all tickets, separated by ticket status
#      statuses: New, In Progress, Done, Invalid
def main(request):
    tickets = Ticket.objects.all()
    new = tickets.filter(status='New')
    assigned = tickets.filter(status='In Progress')
    done = tickets.filter(status='Done')
    invalid = tickets.filter(status='Invalid')
    return render(request, 'main.html', {'new': new, 'in_progress': assigned, 'done': done, 'invalid': invalid})


# TODO filing and creating tickets
def create_ticket(request):
    if request.method == 'POST':
        form =
    return render(request, 'form.html', {'form': form})


# TODO ticket detail page
def ticket_details(request, ticket_id):
    return render(request, '', {})


# TODO edit tickets, limited to only title and description
def edit_ticket(request, ticket_id):
    return render(request, '', {})


# TODO assign a ticket to currently logged in user, which changes status to in progress
def assign(request, ticket_id):
    return


# TODO mark ticket as invalid
def invalidate(request, ticket_id):
    return


# TODO mark ticket as complete
def complete(request, ticket_id):
    return



