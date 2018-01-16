#import urllib2

import json
import requests

key = "3d67bfba0d293516"
country = 'Jamaica'
city = 'Montego_bay'

def weather_update(key, country, city):
    f = requests.get('http://api.wunderground.com/api/'+ key +'/geolookup/conditions/forcast/q/'+country+'/'+city+'.json')
    json_string = f.json()
    #print(type(json_string))
    #parsed_json = json.dumps(json_string)
    return json_string
    f.close()

json_s = weather_update(key, country, city)

location = json_s['location']['city']
feels = int(json_s['current_observation']['feelslike_f'])
 
temp_c = json_s['current_observation']['temp_c']
str(temp_c)
#print(type(temp_c))
condition = json_s['current_observation']['weather']
country = json_s['location']['country_name']
#print("Current temperature in %s is: %dC" %(location, temp_c))
#print("Current condition is %s " %(condition))
#print("Feels like %sF" %(feels))

#todo convert to celcius.
#

def cel_to_far(c):
    #int(celcius)
    cel = (5/9*(c-32))
    #print(celcius)  
    return cel  

f = int(cel_to_far(feels))


######################################
import tkinter

window = tkinter.Tk()


window.title("Today's Weather")
window.geometry('300x150')
#window.wm_iconbitmap('alien.ico')

lbl = tkinter.Label(window, text=city+": " + str(temp_c))
lbl2 = tkinter.Label(window, text="Current Condition: "+ condition)
lbl3 = tkinter.Label(window, text="Feels Like: "+ str(f))
btn = tkinter.Button(window, text="Refresh", command=weather_update(key, country, city))
#ent = tkinter.Entry(window)

lbl.pack()
lbl2.pack()
lbl3.pack()
btn.pack()

window.update_idletasks()
########################################

