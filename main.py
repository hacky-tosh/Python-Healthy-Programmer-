# Healthy Proggrammer
'''

9 am - 5 pm
water - water.mp3 (3.5 liter ) every 20 min to stop music enter input drank . then log in text file
eyes - eyes.mp3 in every 30 min to stop music input  eydone . then log in text file
physical activites - physical.mp3  every 45 minutes to stop music input exdone

water to drink 4 liters
one time drinking 200 ml  = means 20 times * 200ml = 4 liter

'''

from pygame import mixer
import time , datetime

def getdate():
    return datetime.datetime.now()

def water():
    # starting the mixer
    mixer.init()
    # loading sound track
    mixer.music.load("water.mp3")
    # music volume
    mixer.music.set_volume(0.9)
    # starting the music
    mixer.music.play()

    while True:
         print("Drink Water")
         print(" enter DRANK to stop music")
         water_input = input()
         if water_input == "DRANK" or water_input == "drank":
             mixer.music.stop()
             log_file = open("water.txt", "a")
             log_file.write("TIME = " +str(getdate()) + "\n")
             log_file.close()
             break
         time.sleep(600)


def eyes():
    # starting the mixer
    mixer.init()
    # loading sound track
    mixer.music.load("eyes.mp3")
    # music volume
    mixer.music.set_volume(0.9)
    # starting the music
    mixer.music.play()

    while True:
        print("Do Eye Exersise")
         print(" enter eydone to stop music")
         water_input = input()
         if water_input == "EYDONE" or water_input == "eydone":
             mixer.music.stop()
             log_file2 = open("eyes.txt", "a")
             log_file2.write("TIME = " +str(getdate()) + "\n")
             log_file2.close()
             break
         time.sleep(600)


def physical():
    # starting the mixer
    mixer.init()
    # loading sound track
    mixer.music.load("physical.mp3")
    # music volume
    mixer.music.set_volume(0.9)
    # starting the music
    mixer.music.play()

    while True:
        print("Do Exersise")
        print(" enter exdone to stop music")
        water_input = input()
        if water_input == "EXDONE" or water_input == "exdone":
            mixer.music.stop()
            log_file3 = open("physical.txt", "a")
            log_file3.write("TIME = " + str(getdate()) + "\n")
            log_file3.close()
            break
        time.sleep(600)

print("Ashutosh's Python Healthy Proggrammer ")

name = input("Enter Your Name  : ")
print(f"Wellcome To Ofiice {name.capitalize()} ")
print("Office Timing 9:00 AM TO 5:00 PM ")

water1  = 0

while(water1<2):
    print("Next Task in 30 sec ")
    # sleep time in sec
    time.sleep(10)
    water()
    print("next task in 30 sec ")
    time.sleep(10)
    eyes()
    print("next task in 30 sec")
    time.sleep(10)
    physical()
    water1 += 1
