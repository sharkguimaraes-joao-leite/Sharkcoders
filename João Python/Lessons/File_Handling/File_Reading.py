#Pyhton Reading Files (txt, json, csv)
#P.S: For this code to work correctly, you need to go to the file_writing file and run the code there
import json
import csv

file_path = "Lessons\\File_Handling\\teste.txt"

try:
    with open(file_path, mode = "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You have no permission to read that file")
print("--------------------------------")

#------------------------------------------------------------------------------------

file_path2 = "Lessons\\File_Handling\\employee.json"

try:
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You don't have permission to read that file")
print("--------------------------------------------")

#-------------------------------------------------------------------------------------------

file_path3 = "Lessons\\File_Handling\\employees.csv"

try:
    with open(file_path3, "r") as file:
        content = csv.reader(file)
        for x in content:
            print(x)
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("You don't have permission to read that file")