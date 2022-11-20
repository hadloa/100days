import requests
from datetime import datetime
import smtplib
from time import sleep

LAT_HOME = 44.043662
LONG_HOME = -122.951852

my_email = "booogiemonster@gmail.com"
password = 'wjbbkqpifdfqxqnj'



def is_near():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()["iss_position"]

    long = float(data['longitude'])
    lat = float(data['latitude'])

    lat_near = LAT_HOME <= (lat + 5) and LAT_HOME >= (long - 5)
    long_near = LONG_HOME <= (lat + 5) and LONG_HOME >= (long - 5)

    if lat_near and long_near:
        #print("Near")
        return True
    else:
        #print('not near')
        return False


def is_night():
    param_sunset = {"lat": LAT_HOME,
                    "long": LONG_HOME,
                    "formatted": 0}
    response_sunset = requests.get(url='https://api.sunrise-sunset.org/json', params=param_sunset)
    data_sunset = response_sunset.json()

    sunrise = int(data_sunset['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data_sunset['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if time_now > sunset or time_now < sunrise:
        #print('dark')
        return True
    else:
        #print('light')
        return False


def send_email(message='The ISS is overhead!', to_email='andrewdhadlock@gmail.com', subject='ISS Overhead'):
    email = f"Subject: {subject}\n\n" \
            f"{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)



def main():
    if is_night() and is_near():
        send_email()
        print('email sent',  datetime.now())
    else:
        print('not sent',  datetime.now())
    sleep(60)
    main()

main()
