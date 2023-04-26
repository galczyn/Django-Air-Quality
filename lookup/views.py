from django.shortcuts import render
import json
import requests

def home(request):
    api_request = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    air_quality_data = []
    stations = api["stations"]

    for station in stations:
        station_id = station["id"]
        url = f"https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}"
        response = requests.get(url)
        try:
            station_air_quality_data = json.loads(response.content)
            air_quality_data.append({
                "stationId": station_id,
                "values": station_air_quality_data,
            })
        except Exception as e:
            air_quality_data.append({
                "stationId": station_id,
                "values": "Error...",
            })

    return render(request, 'home.html', {'api': api, 'air_quality_data': air_quality_data})


def about(request):
    return render(request, 'about.html', {})
