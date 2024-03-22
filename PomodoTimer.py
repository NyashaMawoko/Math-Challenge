import time 
from pygame import mixer 

#countdown timer
def countdown(t):
    while t:
    mins = t //60
    sec = t % 60
    timer = "{:02d}:{:02d}".format(mins, secs)
 print(timer, end="\r")
 time.sleep(1)
 t -= 1
print("Take off!")

t = int(input("How many seconds do you want to set the timer for?"))
countdown(int(t))


#pomodoro timer
def pomodoro():
    print("Pomodoro starts now!")
    for i in range(4):
        t = 25 *60
        while t :
            mins = t // 60
            secs = t % 60
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print("Time for a break!")
        mixer.init()
        mixer.music.load("C:\Users\mawok\OneDrive\Desktop\music\LEEONA_-_LEEONA_-_Do_I.mp3")
        mixer.music.play()
        time.sleep(4)
        mixer.music.stop()
        
        t = 5 * 60
        while t:
            mins = t // 60
            secs = t % 60
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print("Let\'s get back to work!")
        mixer.init()
        mixer.music.load("C:\Users\mawok\OneDrive\Desktop\music\LEEONA_-_LEEONA_-_Do_I.mp3")
        mixer.music.play()
        time.sleep(4)
        mixer.music.stop()
Pomodoro()       


