import os
from datetime import datetime

file_with_date = datetime.now()
file_path = r"D:\python_file\\"
final_file_name = file_path+"File-"+file_with_date.strftime("%d-%m-%Y-%H-%M-%S")+".txt"
takeFilePath = input("Enter File path and name = ")
if os.path.exists(takeFilePath):
    print("File already present")
    print("Do you want to create it?y/n")
    yes = input("Write Y = ")
    if(yes=='y'):
        with open(final_file_name, "w") as fp:
            print("File created successfully")
    else:
        print("create file later")
else:
    with open(final_file_name, "w") as fp:
        print("File created successfully")