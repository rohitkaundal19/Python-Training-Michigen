import urllib.request, urllib.parse, urllib.error
import json
import ssl

# API Keys - for google API we need to pay,
# Therefore we are using API provided by Dr Chuck "the instructor"

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore the SSL certificate issues if any

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    # Get the location from the User
    location = input ("Enter Location: ")
    if len(location) < 1:
        break

    # Declaring Dictionary to pass Location and key
    parms = dict()
    parms['address'] = location
    parms['key'] = api_key

    url = (service_url + urllib.parse.urlencode(parms))
    #print('Retrieving', url)

    fhand = urllib.request.urlopen(url).read()

    file = fhand.decode()
    print ('Retrieved',len(file),'characters')

    try:
        info = json.loads(file)
    except:
        info = None

    #print (file)
    print("Complete Address: ", info["results"][0]["formatted_address"][:])
    print("Latitude        : ", info["results"][0]["geometry"]["location"]["lat"])
    print("Longitude       : ", info["results"][0]["geometry"]["location"]["lng"])
    print("Type of Place   : ", info["results"][0]["types"][:])
    print ("Place Id        : ", info["results"][0]["place_id"])
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
