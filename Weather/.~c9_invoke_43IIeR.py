import json
import urllib2
import Epic


def location(x):
    url = 'https://api.apixu.com/v1/forecast.json?key=7d58e084d8de4f73916223427172903&q=' + x
    jsonTxt = urllib2.urlopen(url).read()
    cities = json.loads(jsonTxt)
   
    return cities

# def temp(m, local):
#     measurement = ""
   
#     if(m == "f"):
#         measurement = local["current"]["temp_f"] 

        
#         return (measurment)
#     elif(m == "c"):
#         measurement =  local["current"]["temp_c"] 
        
#         return (measurement)

def main():
    another = "y"
    while(another == "y"):
        cityname = Epic.userString("Please enter a zipcode or city name: ")
        local = location(cityname)
        print ""
        print "Here is the current weather for %s, %s." % (local["location"]["name"], local["location"]["region"])
        m = Epic.userString("Would you like to see the temperature in F or C?")
        print "%s and %s degrees %s" % (local["current"]["condition"]["text"], temp(m, local))
        print "It actually feels like %s (F)" % local["current"]["feelslike_f"]
        print ""
        another = Epic.userString("Want to check another location? (y/n)")
        if(another != "y"):
            print "please enter (y/n)"

main()