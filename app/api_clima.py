import requests

api_key = ''
city_name = 'São Paulo'


def get_coordenadas(city_name, api_key, limit=1):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()

        return {
            'latitude': dados[0]['lat'],
            'longitude': dados[0]['lon'],
            'cidade': dados[0]['name'],
            'estado': dados[0]['state']
        }
    else:
        return f"Error: {response.status_code} - {response.text}"
    
def get_clima_via_coordenadas(lat, lon, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()

        return {
            'Bairro Baseado': dados['name'],
            'Temperatura Atual': dados['main']['temp']
        }
    
    else:
        return f"Error: {response.status_code} - {response.text}"

    

coordenadas = get_coordenadas('São Paulo', api_key)
clima = get_clima_via_coordenadas(coordenadas['latitude'], coordenadas['longitude'], api_key)
print(clima)