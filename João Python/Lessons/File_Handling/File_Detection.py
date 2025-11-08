#Python File Detection with the OS model
import os

file_path = "c:\\Users\\Aluno EDAH\\Documents\\bi farfetch'd.png"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print(f"'{file_path}' is a file")
    elif os.path.isdir(file_path):
        print(f"'{file_path}' is a directory")
else:
    print("That location doesn't exist")