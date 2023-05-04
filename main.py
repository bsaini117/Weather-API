import requests
from twilio.rest import Client

twilio_sid = "ACc29cfb9acc94e19b7d7196775d863aba"
auth_token = "403ab48cbc17de3f3a1385f1bad7e135"

api_key = "b647705466719a737a167601b28aefa3"
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





