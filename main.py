import requests
from twilio.rest import Client

twilio_sid = "INSERT ID"
auth_token = "INSERT TOKEN"

api_key = "INSERT KEY"
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"


weather_params = {"lat": 38.712238,
                  "lon": -90.468208,
                  "appid": api_key}


response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_Data = data["list"]
twelve_hour_forcast = weather_Data[0:4]


will_rain = False
for data in twelve_hour_forcast:
    id = data['weather'][0]['id']
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_sid, auth_token)
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='7262042176',
        to='2406189060'
    )
    print(message.status)





