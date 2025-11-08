#Time = Functions with the "Import Time" function 
import time

time.sleep(3)

print("Time is up!")

while True:
    try:
        my_time = int(input("How long would you like the timer to be in seconds?: "))
        break
    except ValueError:
        print("Write a number")

for x in range(my_time, 0, -1):
    seconds = int(x) % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!")