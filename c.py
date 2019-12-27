import os
path=os.getcwd()
a=os.popen("mkdir dell")
a.close()
b=os.popen("ls -lish")
for i in b:
    c=i.split(" ")
    print("folder name",c[-1])
b.close()
list_dir=os.listdir(path)
print(list_dir)
if "dell" in list_dir:
    print("1st folder created success")
d=os.rename("dell","hp")
list_dir1=os.listdir(path)
print("new list ",list_dir1)
if "hp" in list_dir1:
    print("rename success")
e=os.chdir(path+"/hp")
f=os.popen("touch lap tab")
f.close()
f1=os.popen("ls -lish")
for i in f1:
    g=i.split(" ")
    print("file is",g[-1])
path1=os.getcwd()
list_file=os.listdir(path1)
print("list of file in hp",list_file)
if "lap" and "tab" in list_file:
    print("file creation success")
h=os.chdir(path)
j=os.popen("mkdir netapp")
j.close()
list_dir2=os.listdir(path)
print(list_dir2)
if "netapp" in list_dir2:
    print("2nd folder created success")
k=os.chdir(path+"/hp")
m=os.listdir(path1)
pat=path+"/netapp"
for i in m:
    z=os.popen("cp "+i+" "+pat)
    z.close()
q=os.listdir(pat)
print("netapp contains",q)
if "lap" and "tab" in q:
    print("files are copied from hp to netapp success")
n=os.chdir(path)
s=os.popen("rm -rf hp netapp")
s.close()
t=os.listdir(path)
print("updated list is ",t)
if "hp" and "netapp" not in t:
    print("folder deleted successfully")

