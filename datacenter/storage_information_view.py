from datacenter.models import Visit
from django.shortcuts import render
from django import utils


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        visit_info = {
            "who_entered": visit.passcard.owner_name,
            "entered_at": utils.timezone.localtime(visit.entered_at),
            "duration": visit.format_duration(visit.get_duration()),
        }
        non_closed_visits.append(visit_info)
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
