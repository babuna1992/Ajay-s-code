import os 
a=os.popen("touch aj")
a=os.popen("ls -lish")
for i in a:
    b=i.split(" ")
    file_name=b[-1]
a.close()
path=os.getcwd()

file_list=os.listdir(path)
print("file list",file_list)
if "aj" in file_list:
    print("file creation success")
d=os.rename("aj","param")
file_list1 = os.listdir(path)
print("new file list",file_list1)
if "param" in file_list1:
    print("rename success")
#os.popen("touch sandip")
c=os.popen("cp param sandip")
file_list2=os.listdir(path)
print("new file list",file_list2)
if "sandip" in file_list2:
    print("copy success")
file_path = os.path.join(path,"sandip")
print("File path is: ",file_path)
print("current working directory is: ",path)
command = "rm "+file_path
print("Command is: ", command)
f = os.popen(command)
f.close()
file_list3=os.listdir(path)
print("new file list",file_list3)
if "sandip" not in file_list3:
    print("delte file sandip success")


