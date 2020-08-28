from django.shortcuts import render
from bugtrack.models import Ticket
from django.shortcuts import HttpResponseRedirect, reverse
from bugtrack.forms import NewTicketForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def main(request):
    tickets = Ticket.objects.all()
    new = tickets.filter(status='New')
    assigned = tickets.filter(status='In Progress')
    done = tickets.filter(status='Done')
    invalid = tickets.filter(status='Invalid')
    return render(request, 'main.html', {'new': new, 'in_progress': assigned, 'done': done, 'invalid': invalid})


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                status='New',
                created_by=request.user,
                assigned_to=None,
                completed_by=None
            )
            return HttpResponseRedirect(reverse('main'))
    form = NewTicketForm()
    return render(request, 'form.html', {'form': form, 'page': 'Create New Ticket'})


@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_details.html', {'ticket': ticket})


@login_required
def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = NewTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data.get('title')
            ticket.description = data.get('description')
            ticket.save()
            return HttpResponseRedirect(reverse('ticket_details'))
    data = {'title': ticket.title, 'description': ticket.description}
    form = NewTicketForm(initial=data)
    return render(request, 'form.html', {'form': form, 'page': 'Edit Ticket'})


@login_required
def assign(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def invalidate(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = 'Invalid'
    ticket.assigned_to = None
    ticket.completed_by = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def complete(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = 'Done'
    ticket.completed_by = ticket.assigned_to
    ticket.assigned_to = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



