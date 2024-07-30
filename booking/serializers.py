from rest_framework import serializers

from booking.models import Trip


class TripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'destination', 'departure_date',
                  'return_date', 'number_of_travelers']
