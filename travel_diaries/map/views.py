import folium
from django.http import HttpResponse
from map.models import Location

def map_page(request):
    center = (13.133932434766733, 16.103938729508073)
    folium_map = folium.Map(location=center, zoom_start=2)
    return HttpResponse(folium_map.get_root().render())