from os.path import dirname, join
import os

current_dir = dirname(__file__)

print(os.getcwd()) #nos da el home

#os.mkdir(join(current_dir,"dir3"))
os.chdir(join(current_dir,"dir3"))
print(os.getcwd())
os.mkdir("newer_dir")

os.rmdir("newer_dir")

print(os.listdir("/workspaces/CourseraPython/Interact with Operative System/Week 2/ManagingFilesAndDirectories/dir1"))


dir = "/workspaces/CourseraPython/Interact with Operative System/Week 2/ManagingFilesAndDirectories/dir1"

for name in os.listdir(dir):
    fullname=os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} es una carpeta".format(fullname))
    else:
        print("{} es un archivo".format(fullname))
    