import requests
import json
from django.core.management.base import BaseCommand
from lookup.models import Station

class Command(BaseCommand):
    help = "Populate stations table with data from API."

    def handle(self, *args, **options):
        url = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
        response = requests.get(url)
        data = json.loads(response.content)

        for station_data in data:
            station = Station(
                id=station_data['id'],
                station_name=station_data['stationName'],
                city_name=station_data['city']['name'],
                latitude=station_data['gegrLat'],
                longitude=station_data['gegrLon']
            )
            station.save()
            self.stdout.write(self.style.SUCCESS(f"Added station {station.id}: {station.station_name}"))
