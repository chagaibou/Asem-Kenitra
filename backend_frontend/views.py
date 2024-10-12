from django.shortcuts import render, get_object_or_404
from backend_frontend.models import Evenement
# Create your views here.

def home_view(request):
    events = Evenement.objects.all()
    last = Evenement.objects.last()

    return render(request,'backend_frontend/home.html',{'last':last})
def evenement_list_view(request):
    events = Evenement.objects.all()

    return render(request,'backend_frontend/evenement.html',{'events': events})

def evenement_detail_view(request,event_id):
    event = get_object_or_404(Evenement,id=event_id)

    return render(request,'backend_frontend/evenement_detail.html',{'event':event})
def a_propos_view(request):
    return render(request,'backend_frontend/apropos.html')


def infos_administrative_view(request):
    return render(request,'backend_frontend/infos_administratives.html')