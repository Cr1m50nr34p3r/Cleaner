import os,sys,subprocess
from os import path
import shutil
PATH="C:/Users/aksha/Downloads"
os.chdir(PATH)
files=os.listdir(PATH)
for i in files:
    print(i)
rm=input("Files to Del: ")
if rm=="all":
    for j in files:
        os.remove(i)
    sys.exit("Work done")
else:
    rm=rm.split(',')
for r in rm:
    if r in files:
        os.remove(path._getfullpathname(r))
        print(f"{r} is removed succesfully")
    else:
        print(f"file {r} not found Moving on to others")
files = os.listdir(PATH)
if len(files)>=1:
    for i in files:
        print(i)
    for f in files:
        folder=input(f"where do you want to store {f}: ")
        os.chdir("C:/Users/aksha/Desktop")
        if path.isdir(folder):
            folder_path=path.realpath(folder)
            os.chdir(PATH)
            shutil.move(f,folder_path)
        else:
            os.mkdir(folder)
            folder_path = path.realpath(folder)
            os.chdir(PATH)
            shutil.move(f,folder_path)
        
            
