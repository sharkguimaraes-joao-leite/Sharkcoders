#How to access the computer's  time and date using the datetime module
import datetime
import pygame
import time

date = datetime.date.today()
date = str(date)
date = date.replace("-", "/")

print(f"You're running this code on {date}, ain't ya?")
print("--------------------------------")

time_now = datetime.datetime.now()
time_now = time_now.strftime("%H:%M:%S %d/%m/%Y")

print(f"Time now: {time_now}")
print("--------------------------------")

#Exercise 1 = Event reminder

time_now = datetime.datetime.now()
target = datetime.datetime(year = 2025, month = 10, day = 16, hour = 12, minute = 00, second = 00)

if target < time_now:
    print("Pokémon Legends Z-A is out now, GO PLAY IT!")
else:
    print("Pokémon Legends Z-A isn't out yet, sad :(")

som = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Audio\\1-17. Accumula Town.mp3"
mae = datetime.datetime(year = 2025, month = 11, day = 8)

if mae == date:
    print("Feliz aniversário, mãe!")
    pygame.mixer.init()
    pygame.mixer.music.load(som)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
else:
    pass