#SatyamRaina
#Libraries
import RPi.GPIO as GPIO        #assigning RPi.GPIO as GPIO
import time                    #to access time related functions

#Defining Pins as on Raspberry Pi Not GPIO pINS
buzzer = 10
GPIO_TRIGGER = 23
GPIO_ECHO = 32

GPIO.setwarnings(False)        #ignore warnings
GPIO.setmode(GPIO.BOARD)       #Let the program know hatpin name convention BOARD referring the number of the pin in the plug
GPIO.setup(buzzer, GPIO.OUT)

#Duty cycle of GPIO output signal controls the pitch of buzzer
buzz = GPIO.PWM(10, 100)        #Channel = 10, Frequency = 100

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, GPIO.LOW)   #Let the program know hatpin name convention BOARD referring the number of the pin in the plug
time.sleep(1)                         #delay

def terminate():
    buzz.stop()
    GPIO.cleanup()

try:
    while True:
        #Let the program know hatpin name convention BOARD referring the number of the pin in the plug
        GPIO.output(GPIO_TRIGGER, GPIO.HIGH)

        #set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, GPIO.LOW)

        #On and Off duration relationship, initialized from 0
        dutyCycle = 0

        buzz.start(dutyCycle)

        #save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            InitialTime = time.time()

        #save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            FinalTime = time.time()
        
        #time difference between start and arrival
        TimeGap = FinalTime - InitialTime
        #multiply with the sonic speed(34300 cm/s)
        #and divide by 2, becasue there and back

        distance = (TimeGap * 34300) / 2

        print(f"Distance: {distance} cm")

        if distance <= 25 and distance >= 0:
            val = round((25-distance)*4)
            buzz.ChangeDutyCycle(val)
            time.sleep(0.4)

#Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")

terminate()
#Satyam Raina

 


