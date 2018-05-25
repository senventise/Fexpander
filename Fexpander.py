import os
from os.path import exists
from dirTest import file_name as fn

def autoCompelete(path,name):
	files=fn(path)
	boolean=False
	index=[]
	j=0
	for i in range(len(files)):
		boolean=name in files[i]
		if(boolean): 
			index.append(i)
			j+=1
			print(str(j)+":"+files[i]+"  ")
	a=int(input("--> "))-1
	return files[index[a]]

#get file's path andi size
path=input("The path:\n")
files=fn(path)
name=input("File name:\n")
exist=exists(path+"/"+name)
if(not exist):
	name=autoCompelete(path,name)
mfile=open(path+"/"+name,"rb")
msize=len(mfile.read())/1024/1024
mfile.close()
print("The size is %s"%(msize))
size=input("The size you want to reach(MB):\n")

"""def autoCompelete(path,name):
	files=fn(path)
	boolean=False
	index=[]
	j=0
	for i in range(len(files)):
		boolean=name in files[i]
		if(boolean):
			index.append(i)
			j+=1
			print(j+":"+files[i]+"  ")
	a=int(input("--> "))-1
	return files[index[a]]	
"""

def expand(fpath,size):
    fpath=str(fpath)
    size=(float(size))#Mb
    sizemb=size
    size*=1024#Kb
    size*=1024#bytes
    aimbytes=int(size)
    print("%r bytes(%r MB)"%(size,sizemb))
    file=open(fpath,"rb")
    bytesalready=len(file.read())
    file.close()
    if(aimbytes>=bytesalready):
        appendbytes=aimbytes-bytesalready
        temp=bytes(appendbytes)
        file=open(fpath,"ab")
        file.write(temp)
        file.close()
    else:
        print("Wrong input!")



#main function
if(exists(path)):
    print("The path exists.")
    expand((path+"/"+name),size)
    print("%r MB was written"%size)
else:
    print("Wrong path!")

