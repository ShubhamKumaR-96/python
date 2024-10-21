import os

#  SELECT THE DIRECTORY WHOSE CONTENT YOU WANT TO LIST 
directory_path ='/Data_Enginnering'

contents=os.listdir(directory_path);

for item in contents:
    print(item)


