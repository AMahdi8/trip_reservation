from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.viewsets import ModelViewSet

from .serializers import TripSerializers
from .forms import TripForm
from .models import Trip


def trip_list(request):
    trips = Trip.objects.all().order_by('departure_date')
    context = {
        'trips': trips
    }
    return render(request, 'booking/list_trips.html', context)


def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm()

    return render(request, "booking/create_trip.html", {"form": form})


def update_trip(request, pk):
    trip = get_object_or_404(Trip, id=pk)
    form = TripForm(request.POST or None, instance=trip)

    if form.is_valid():
        form.save()
        return redirect('trip_list')

    return render(request, 'booking/update_trip.html', {'form': form})


def delete_trip(request, pk):
    trip = get_object_or_404(Trip, id=pk)

    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')

    return render(request, 'booking/confirm_delete.html', {'trip': trip})


class TripViewSet(ModelViewSet):
    queryset = Trip.objects.all().order_by('departure_date')
    serializer_class = TripSerializers
