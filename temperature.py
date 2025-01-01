import adafruit_thermistor
import board
import time

thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 22, 3950)
SLEEPTIME = 10

#output_filename = 'temperatures.csv'

#with open(output_filename, "w") as outfile:
#    outfile.write("Time,Temperature\n")

seconds = 0

while True:
    temp = thermistor.temperature
    print("%d: %0.2fC" % (seconds, temp))
#    with open(output_filename, "a") as outfile:
#        outfile.write("%s,%0.2f\n" % (now, temp))
    time.sleep(SLEEPTIME)
    seconds += SLEEPTIME
