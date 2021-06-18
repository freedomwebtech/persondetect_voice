import os
import subprocess
from gtts import gTTS



def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")




def recog():
    b=os.system("face_recognition known_people uknown_people/ | cut -d ',' -f2 > test.txt")

#    with open("test.txt", "r") as f:
#         for line in f:
#             speak(line)
             

    file1 = open('test.txt', 'r')
    Lines = file1.readlines()
    count = 0

    for person in Lines:
         count += 1
         speak(("person {}: {}".format(count, person.strip())).replace("_", " "))




recog()



