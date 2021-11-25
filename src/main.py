import requests

from datetime import datetime
import smtplib

# defauld constant
my_latitude = 22.841930
my_longitude = 89.558060

defult_location = {
    'lat':my_latitude,
    'lng':my_longitude
}
my_gmail ="rpg736tanvir@gmail.com"
my_password ="01955005706#@"

def sendMail():
    # creting the server connectionof the mail
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        # supporting the authentication
        connection.starttls()
        # login to my account
        connection.login(user=my_gmail,password=my_password)
        # sending the mail
        connection.sendmail(from_addr=my_gmail,to_addrs='tanvir15-13433@diu.edu.bd',msg=f"Subject: Seterlite detected \n\n\nPlease Look UP")
    

def isNearTheLocation():
    
    if my_latitude-5<=latitude<=my_latitude+5 and my_longitude-5<=logitude<=my_longitude+5:
        return True
    else:
        return False



def isLocated():
    if my_latitude == latitude and my_longitude == logitude:
        return True
    else:
        return False

def isDark():
    if current_time.hour >= sunset or current_time.hour<=sunrise:
        return True
    else:
        return False



response = requests.get(url='http://api.open-notify.org/iss-now.json')


# creating the error code if something goes wrong
response.raise_for_status()

# now i am goig to parse the endpoint from the url
data = response.json()

latitude = float(data['iss_position']['latitude'])
logitude = float(data['iss_position']['longitude'])
print(latitude,logitude)

response2 = requests.get(url=f'https://api.sunrise-sunset.org/json?{defult_location}&formatted=0')
# print(response2.status_code)
response2.raise_for_status()

data2 = response2.json()
# print(data2)
sunrise = int(data2['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data2['results']['sunset'].split("T")[1].split(":")[0])
current_time = datetime.now()
print(sunrise)
print(sunset)
print(current_time.hour)
if (isLocated() and isDark()) or (isNearTheLocation() and isDark()):
    sendMail()
else:
    print("There stil time")


