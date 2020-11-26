from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits_by_this_passcard = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in  visits_by_this_passcard:
        visit_info = {
            "entered_at": visit.entered_at,
            "duration": visit.format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long(hours_limit=1)
        }
        this_passcard_visits.append(visit_info)
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
