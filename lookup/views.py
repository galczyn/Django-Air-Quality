from django.shortcuts import render
import json
import requests

def home(request):
    api_request = requests.get("https://api.gios.gov.pl/pjp-api/rest/station/findAll")

    try:
        stations = json.loads(api_request.content)
    except Exception as e:
        stations = "Error..."

    # return render(request, 'home.html', {'api': api})

    air_quality_data = []
    # stations = api["stations"]

    for station in stations:
        station_id = station["id"]
        # station_id = stations[1]['id']
        url = f"https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}"
        response = requests.get(url)
        try:
            station_air_quality_data = json.loads(response.content)
            # print(station_air_quality_data)
            air_quality_data.append(station_air_quality_data)
            print(air_quality_data[-1])
        except Exception as e:
            air_quality_data.append({
                "stationId": station_id,
                "values": "Error...",
            })
    print(station_air_quality_data)
    return render(request, 'home.html', {'stations': stations, 'air_quality_data' : air_quality_data})

def about(request):
    return render(request, 'about.html', {})
