from django.shortcuts import render, redirect, get_object_or_404
from .models import Sports


def home(request):
    return render(request, 'index.html')


def sports_list(request):
    sports = Sports.objects.all()
    ctx = {'sports': sports}
    return render(request, 'sports/sports-list.html', ctx)


def sports_create(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        if event_name and location and date and sport_type:
            Sports.objects.create(
                event_name = event_name,
                location = location,
                date = date,
                sport_type = sport_type,
        )
        return redirect('sports:list')
    return render(request, 'sports/sports-form.html')


def sports_detail(request, pk):
    sports = get_object_or_404(Sports, pk=pk)
    ctx = {'sports': sports}
    return render(request, 'sports/detail.html', ctx)

def sports_update(request, pk):
    sports = get_object_or_404(Sports, pk=pk)
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        if event_name and location and date and sport_type:
            sports.event_name = event_name
            sports.location = location
            sports.date = date
            sports.sport_type = sport_type
            sports.save()
            return redirect(sports.get_detail_url())
    ctx = {'sports': sports}
    return render(request, 'sports/sports-form', ctx)



def sports_delete(request, pk):
    sports = get_object_or_404(Sports, pk=pk)
    sports.delete()
    return redirect('sports:list')

