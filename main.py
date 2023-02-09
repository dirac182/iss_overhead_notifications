import requests
from datetime import datetime, timezone
import time
import smtplib

MY_LAT = 26.191930 # Your latitude
MY_LONG = -98.284820 # Your longitude

def check_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT -5 <= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG +5:
        return True
    else:
        return False

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now(timezone.utc)
def check_night():
    if sunset <= time_now.hour <= sunrise:
        return True
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="busjackson37@gmail.com", password="yqhpkksgkiwllbob")
        connection.sendmail(to_addrs="dmorin9696@yahoo.com", from_addr="busjackson37@gmail.com",
                            msg="Subject: Look Up!! \n\n The International Space Station is above you! Try to spot it!")
while True:
    time.sleep(60)
    if check_iss() and check_night():
        send_email()



