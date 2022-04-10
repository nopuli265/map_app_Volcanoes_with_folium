import folium
import pandas
data= pandas.read_csv('Volcanoes.txt')
lat= list(data['LAT'])
lon=list(data['LON'])
elev= list(data['ELEV'])

def color_producer(par):
    if par< 1000:
        return 'green'
    elif par>1000 and par<3000:
        return 'orange'
    else:
        return 'red'
map=folium.Map(location=[38.8,-99.09], zoom_start=6, tiles="Stamen Terrain")
fgv= folium.FeatureGroup(name="Volcanoes")

# for lt, ln, el in zip(lat,lon, elev):
#     fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup((str(el)+" m"),parse_html=True), icon= folium.Icon(color=color_producer(el))))
for lt, ln, el in zip(lat,lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=folium.Popup((str(el)+" m"),parse_html=True), fill_color=color_producer(el),color='grey', fill=True,fill_opacity=0.7))
fgp= folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':"red" if x['properties']['POP2005']<10000000 else 'green'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map1.html')