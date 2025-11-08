#Basic alarm clock using the Datetime module
import time
import datetime
import pygame #For sfx
charas = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ';', '<', '=',
          '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

#-------------------------------------------------------------------------------------------
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound = "c:\\Users\\Aluno EDAH\\Downloads\\2-02. Driftveil City.mp3"
    running = True
    while running:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        time.sleep(1)
        if time_now == alarm_time:
            print("WAKE UP, YOU BASTARD!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            running = False

alarm_time = input("Enter the alarm time (HH:MM:SS): ")
set_alarm(alarm_time)