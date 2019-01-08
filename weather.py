from sense_hat import SenseHat
from csv import writer
from datetime import datetime
import csv

sense = SenseHat()
sense.clear()

try:
      
      while True:
          
           temp = (sense.get_temperature())
           temp = (round(temp - 10, 1)) 
           print("Homerseklet C: ",temp)

           humidity = (sense.get_humidity()) 
           humidity = (round(humidity, 1)) 
           print("Paratartalom: ",humidity)  

           pressure = (sense.get_pressure())
           pressure = (round(pressure, 1))
           print("Legnyomas: ",pressure)
           
           hour = (str(datetime.now().strftime("%H:%M")))
           print(hour) 
            
           with open('adat.csv', 'a', newline='') as csvfile:
                thewriter = csv.writer(csvfile)
                thewriter.writerow([hour,temp, humidity,pressure])
                csvfile.close()
                
           
           sense.show_message("Hom.: " + str(temp) + "C  " + "Parat.: " + str(humidity) + " % " + "Legny.: " + str(pressure) + " hPa "
                              + "Ido: " + str(hour), scroll_speed=(0.07), back_colour= [0,0,0], text_colour= [10,150,150],)
           
           
except KeyboardInterrupt:
    sense.clear()