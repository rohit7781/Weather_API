import requests
import smtplib, ssl

APIID = 'GET YOUR OWN API ID'

# UPDATE YOUR OWN LONGITUTE AND LATITUDE
parameter = {
    'lat':26.6476,
    'lon':84.9143,
    'exclude':'current,minutely,hourly',
    'appid':APIID
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameter)

response.raise_for_status()


view = response.json()

code = view['daily'][0]['weather'][0]['id']
condition = view['daily'][0]['weather'][0]['main']
description = view['daily'][0]['weather'][0]['description']
pressure = view['daily'][0]['pressure']
humadity = view['daily'][0]['humidity']
Wind_speed = view['daily'][0]['wind_speed']
min = view['daily'][0]['temp']['min']
max = view['daily'][0]['temp']['max']


# print('Code :',code)
# print('Wheather : ',condition)
# print('Wheather Description : ',description)
# print('Pressure : ',pressure)
# print('Humadity : ', humadity)
# print('Wind Speed(m/sec) : ',Wind_speed)
# print('Min Temp(F) :' ,min)
# print('Max Temp(F) :' ,max)

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "Your email"
receiver_email = 'Reciver eamil'
# receiver_email2 = 'second Reciever email'
password = "YOUR PASSWORD"
message = f"Subject :  Today's Wheather Report \n\nCode : {code}\nWheather : {condition} \nWheather Description : {description}\nPressure(pa) : {pressure}\nHumadity(%) : {humadity}\nWind Speed(m/sec) : {Wind_speed}\nMin Temp(F) : {min}\nMax Temp(F) :{max}"



context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
# with smtplib.SMTP(smtp_server, port) as server:
#     server.starttls(context=context)
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email2, message)