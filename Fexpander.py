import os
from os.path import exists
storage="/storage/emulated/0/"
path=input("Please type in the path:\n"+storage)
path=storage+path
name=input("Please type in the file name:\n")
mf=open(path+"/"+name,"rb")
msize=len(mf.read())/1024/1024
print("the size is %s"%(msize))
size=input("Please type in the size you want to reach(MB):\n")



def expand(fpath,size):
    fpath=str(fpath)
    size=(float(size))#Mb
    sizemb=size
    size*=1024#Kb
    size*=1024#bytes
    aimbytes=int(size)
    print("%r bytes(%r MB) will be written."%(size,sizemb))
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
        print("Your aim size is smaller than the file before.")



#main function
if(exists(path)):
    print("The path exists.")
    expand((path+"/"+name),size)
    print("Done.%r MB was written"%size)
else:
    print("Wrong path!")

