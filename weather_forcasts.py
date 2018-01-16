#import urllib2

import json
import requests

 
key = "3d67bfba0d293516"

# Country name
country = 'Jamaica'

#City name
city = 'Montego_bay'

# function that gets the current weather. Returns a dictionary with Json data.
def weather_update(key, country, city):
    f = requests.get('http://api.wunderground.com/api/'+ key +'/geolookup/conditions/forcast/q/'+country+'/'+city+'.json')
    json_string = f.json()
    return json_string
    f.close()

# Calls the weather function ans store as a dictionary
json_s = weather_update(key, country, city)

# gets the location, real feel and temperature in Celsius.
location = json_s['location']['city']
feels = int(json_s['current_observation']['feelslike_f'])

# temp_c is an int which is converted to string for display
temp_c = json_s['current_observation']['temp_c']
str(temp_c)

# condition and country are strings
condition = json_s['current_observation']['weather']
country = json_s['location']['country_name']

#print("Current temperature in %s is: %dC" %(location, temp_c))
#print("Current condition is %s " %(condition))
#print("Feels like %sF" %(feels))

# function to convert to celcius from Farenheit.
def cel_to_far(c):    
    cel = (5/9*(c-32))  
    return cel  

# call the convertion which produces a float. 
f = int(cel_to_far(feels))


# GUI
######################################
import tkinter

# create a tkinter object
window = tkinter.Tk()

#window title and initial size
window.title("Today's Weather")
window.geometry('300x150')
#window.wm_iconbitmap('alien.ico')

# buttons and labels with data from dictionary
lbl = tkinter.Label(window, text=city+": " + str(temp_c))
lbl2 = tkinter.Label(window, text="Current Condition: "+ condition)
lbl3 = tkinter.Label(window, text="Feels Like: "+ str(f))
btn = tkinter.Button(window, text="Refresh", command=weather_update(key, country, city))

#lbl4 = tkinter.Label(window, text="Please enter the city:")
#ent = tkinter.Entry(window)

lbl.pack()
lbl2.pack()
lbl3.pack()
btn.pack()

window.update_idletasks()
########################################

