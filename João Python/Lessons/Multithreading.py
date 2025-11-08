#Multithreading = Used to perform multiple code at the same time
import threading
import time
import random
#-----------------------------------------------------------------------------
class actions:
    def walk_dog(dog_name):
        time.sleep(8)
        print(f"You walked {dog_name} through the neighborhood. It was fun!")

    def remove_trash():
        time.sleep(2)
        print("You took out the trash. Disgusting...")

    def mail():
        time.sleep(4)
        print("You check your mailbox...")
        time.sleep(1)
        num = random.randint(1, 2)
        if num == 1:
            print("It has some mail inside it!")
        else:
            print("It's empty...")


chore1 =threading.Thread(target = actions.walk_dog, args = ("Link",))
chore1.start()

chore2 =threading.Thread(target = actions.remove_trash())
chore2.start()

chore3 =threading.Thread(target = actions.mail())
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")

#Multithreading let's other code run while another code is running, such as with this example, walking 
#the dog takes 8 seconds, so while those 8 seconds are counting, the code runs the remove_trash() and 
#mail() functions in the meantime.