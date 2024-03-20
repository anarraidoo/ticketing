import string, random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ticketing.models import Ticket


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def index(request):
    return render(request, 'home.html')


def index_jinja(request):
    return render(request, 'jinja2/jinjahome.html')



def show_layout(request):
    return render(request, 'applayout.html')
# def index2(request):
#     return render(request, 'home.html')


def submit(request):
    if request.method == "POST":
        username = request.POST.get('username')
        body = request.POST.get('body')
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("Successfully submitted ticket")
    # new_ticket = Ticket(submitter=randomString(), body="Help, I need help with a bug")
    # new_ticket = Ticket(submitter="Test user", body="Help, I need help with a bug")
    # new_ticket.save()
    return render(request, 'submit.html')


def tickets_raw(request):
    all_tickets = list(Ticket.objects.values())
    return JsonResponse(all_tickets, safe=False)


def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': all_tickets})


def ticket(request, ticket_id):
    selected_ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'ticket.html', {'ticket': selected_ticket})
