import os
path = os.getcwd()
a = os.popen("mkdir p5")
a.close()
b = os.chdir("p5")
for i in range(10):
	d = "aj" + str(i)
	c = os.popen("dd if=/dev/urandom of=d bs=1M count=100")
e=os.popen("ls -lish")
alist=[]
for i in e:
	g=i.split(" ")
	alist.append(g[1])
print(alist)
