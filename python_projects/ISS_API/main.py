import requests
import datetime
import smtplib
import time as t


my_email = "sender_email"
password = "sender_password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data_iss = response.json()
long = float(data_iss["iss_position"]["longitude"])
lat = float(data_iss["iss_position"]["latitude"])

params = {
    "lat": 41.084049,
    "lng": 29.051020,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data_sun = response.json()
sunrise = data_sun["results"]["sunrise"]
sunset = data_sun["results"]["sunset"]

sunrise = int(sunrise.split("T")[1].split(":")[0])+2
sunset = int(sunset.split("T")[1].split(":")[0])+2

time = datetime.datetime.now()


def is_close():
    if params["lat"] < lat+5 and params["lat"] > lat-5 and params["lng"] < long+5 and params["lng"] > long-5:
        return True
    else:
        print("ISS is far away now")


def is_night():
     if not time.hour < sunset and time.hour > sunrise:
         return True
     else:
         print("it's day time")

while True:
    if is_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as bridge:
            bridge.starttls()
            bridge.login(user=my_email, password=password)
            bridge.sendmail(from_addr=my_email, to_addrs="receiving_email",
                            msg=f"Subject:Look up!\n\nNow ISS can be seen from South Campus")
    t.sleep(600)