import os
import subprocess
from gtts import gTTS
from picamera import PiCamera
from time import sleep




def cam():
    camera = PiCamera()
    camera.rotation = 180
    camera.sharpness = 70
    camera.saturation = 50
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/persondetect_voice/unknown_people/image.jpg')
    camera.stop_preview()





def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")




def recog():
    b=os.system("face_recognition known_people unknown_people/ | cut -d ',' -f2 > test.txt")
    file1 = open('test.txt', 'r')
    Lines = file1.readlines()
    count = 0

    for person in Lines:
         count += 1
         speak(("person {}: {}".format(count, person.strip())).replace("_", " "))



cam()
recog()



