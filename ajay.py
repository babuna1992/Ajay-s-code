import os
import logging 
import shutil

logging.info("Step :Create files")

out = os.popen("touch automation")
out = os.popen("ls -lish")
for i in out:
    i = i.split()
print (i)
file_name = i[-1]
print("file name is : ",file_name)
file_list = os.listdir()
print("file list is : ",file_list)
