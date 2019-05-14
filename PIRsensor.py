import time
import datetime
import picamera
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led1 = 17
led2 = 27
pirPin = 26

isInUse = 0

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)

GPIO.output(led1, GPIO.LOW)
GPIO.output(led2, GPIO.HIGH)

def take_still(path):
    with picamera.PiCamera() as camera :
        camera.resolution = (1280, 720)
        now = datetime.datetime.now()
        camera.capture(path + now.isoformat() + ".jpg")
        time.sleep(2)
    print("Picture taken!")

def lights(pirPin):
    global isInUse

    print("Motion Detected!")
    print("Lights on")

    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2, GPIO.LOW)
    start_time = time.time()
    if isInUse == 0:
        isInUse = 1
        take_still("/home/pi/proj/stills/detectedMotionStills/motionCapture");
        isInUse = 0

    print("Lights out")
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.HIGH)

print("Motion tracker")
time.sleep(1)
print("Ready")
start_time = time.time();

while 1:
    try: 
        GPIO.add_event_detect(pirPin, GPIO.RISING, callback=lights)
        i = 1
        while 1:
            elapsed_time = time.time() - start_time
            if elapsed_time > 10 * i and isInUse == 0:
                print(elapsed_time)
                isInUse = 1
                take_still("/home/pi/proj/stills/timedStills/")
                isInUse = 0
                i = i + 1
            if elapsed_time > 60:
                os.system('python zipAndUploadFiles.py')
                print('Backup Done!')
                i = 1
                start_time = time.time()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Quit")
        GPIO.cleanup()
