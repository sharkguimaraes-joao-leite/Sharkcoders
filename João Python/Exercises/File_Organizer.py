import os
import shutil
import time
import pygame
#-----------------------------------------------------------------------------------------------------
categories = {"Images": [".jpg", ".jpeg", ".png", "gif"],
              "Documents": [".pdf", ".docx", ".txt"],
              "Audio": [".mp3", ".wav"],
              "Video": [".mp4", ".avi", ".mov"],
              "Others": []}

ding = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Audio\\ding-36029.mp3"
rolled = "c:\\Users\\Aluno EDAH\\Desktop\\João\\Audio\\Mzg1ODMxNTIzMzg1ODM3_JzthsfvUY24.MP3"
#-------------------------------------------------------------------------------------------------------
def main():
    try:
        print("=== File Organizer ===")
        file = input("Write the path that you want to organize: ")
        for category in categories:
            path_new_file = os.path.join(file, category)
            if not os.path.exists(path_new_file):
                os.mkdir(path_new_file)
        for document in os.listdir(file):
            path_document = os.path.join(file, document)
            if os.path.isfile(path_document):
                name, extension = os.path.splitext(document)
                moved = False
                for category, extensions in categories.items():
                    if extension.lower() in extensions:
                        shutil.move(path_document, os.path.join(file, category, document))
                        moved = True
                        break
                if not moved:
                    shutil.move(path_document, os.path.join(file, "Others", document))
        print("...")
        time.sleep(1)
        pygame.mixer.init()
        pygame.mixer.music.load(ding)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        print("Organization complete!")
        time.sleep(1)
        print("jk get rickrolled noob")
        pygame.mixer.init()
        pygame.mixer.music.load(rolled)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except FileNotFoundError:
        print("File Not Found")

if __name__ == '__main__':
    main()