import shutil
import os

source_path = input("Give the path of the folder you want to backup : ")
back_path = input("Pls give the path of a folder where you want to store the Backup : ")

listOfItems = os.listdir(source_path)

for i in listOfItems:
    FileName, Extension = os.path.splitext(i)
    if(Extension == '' or Extension == 'pc'):
        continue
    path = source_path+'/'+i
    dest_path = back_path+'/'
    shutil.copy(path, dest_path)

print("I am sorting them.")

listOfItems2 = os.listdir(back_path)

for i in listOfItems2:
    FileName, Extension = os.path.splitext(i)
    if(Extension == ''):
        continue

    finalPath = back_path + '/' + Extension
    exist = os.path.exists(finalPath)
    if(exist == False):
        os.mkdir(finalPath)
    shutil.move(back_path+'/'+i, finalPath+'/'+i)

print("Sorted your stuff!")
print("Your files are ready!")