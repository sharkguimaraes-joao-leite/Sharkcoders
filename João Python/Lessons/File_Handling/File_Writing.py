#Python writing files (txt, .json, .csv)

txt_data = "I am rapidly aproaching your location...\n Love: Your worst nightmare"

file_path  = "Lessons\\File_Handling\\teste.txt"

try:
    with open(file_path, mode = "x") as file:
        file.write(txt_data)
    print("Text file has been created")  
except FileExistsError:
    print("That file already exists!")

print("-----------------------------------------")
#There are many diferent modes, "x" = write if file doesn't already exist, "w" = write, "a" = append,...
import json

employee = {"name": "Pomni",
            "age": 25,
            "job": "accountant",
            "gender": "female"}

file_path  = "Lessons\\File_Handling\\employee.json"

try:
    with open(file_path, mode = "x") as file:
        json.dump(employee, file, indent = 4)
    print("Json file has been created")  
except FileExistsError:
    print("That file already exists!")

print("-----------------------")
#------------------------------------------------------------------------------------------------
import csv

employees = [["Name", "Age", "Job", "Gender"],
             ["Jax", 22, "Unemployed", "Male"],
             ["Zooble", 23, "Bartender", "Non-Binary"],
             ["Gangle", 25, "Fast-Food", "Female"]]

file_path  = "Lessons\\File_Handling\\employees.csv"

try:
    with open(file_path, mode = "x", newline = "") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
    print("Csv file has been created")  
except FileExistsError:
    print("That file already exists!")