import os
path = os.getcwd()
a = os.popen("mkdir sambit")
a.close()
b = os.chdir("sambit")
c = os.popen("touch python storage memory")
path1 = os.getcwd()
with open("python","w") as f:
    f.write("sambit is genius")
with open("storage","w") as f:
    f.write("parama is a bad guy")
with open("memory","w") as f:
    f.write("contiguous and non contiguous")
ino_list = []
phy_list = []
log_list = []
d = os.popen("ls -lish")
for i in d:
        e = i.split(" ")
        print("length of line",len(e))
	if len(e)>7:
		ino_list.append(e[0])
		phy_list.append(e[1])
		log_list.append(e[-5])
d.close()
print ("inode list is:",ino_list)
print("physical size list:",phy_list)
print("logical size list:",log_list)

