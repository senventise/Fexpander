import os
import color
from os.path import exists
from dirTest import file_name as fn

def fileList(path):
    files=fn(path)
    for index,item in enumerate(files):
        print(str(index+1)+"\t"+item)
    a=int(input("-->"))
    return files[a-1]

#get file's path and size
path=input("The path:")
files=fn(path)
#name=input("File name:")
name=fileList(path)
mfile=open(path+"/"+name,"rb")
msize=len(mfile.read())/1024/1024
mfile.close()
print(color.generate("\n\n%s"%name,color.color.YELLOW))
print("The size is %s"%(msize))
size=input("The size you want to reach(MB):\n")

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
        print(color.generate("%r MB was written"%size,color.color.GREEN))
    else:
        print(color.generate("Wrong size!",color.color.RED))



#main function
if(exists(path)):
    print(color.generate("The path exists.",color.color.GREEN))
    expand((path+"/"+name),size)
else:
    print(color.generate("Wrong path!",color.color.RED))

