import os
import sys
import color
import time
from os.path import exists
from dirUtils import file_name as fn


class UnexceptedInput(Exception):
    pass


def get_file_name():
    global path, file_name
    try:
        file_name = choose_file(path)
        # return 0
    except UnexceptedInput as info:
        info = str(info)
        if(info == "wrong type"):
            print(color.generate("Wrong type of index,need an integer not the file name!", color.color.RED))
            time.sleep(1)
            fname = get_file_name()
        elif(info == "wrong index"):
            print(color.generate("the index is out of range!", color.color.RED))
            time.sleep(1)
            fname = get_file_name()
        elif(info == "wrong path"):
            print(color.generate("the path does not exists!", color.color.RED))
            time.sleep(1)
            path = input("The path:")
            fname = get_file_name()


def choose_file(mpath):
    try:
        mfiles = fn(mpath)
    except FileNotFoundError:
        raise UnexceptedInput("wrong path")
    for index, item in enumerate(mfiles):
        print(str(index+1)+"\t"+item)
    print(color.generate("\nplease input the index", color.color.YELLOW))
    a = input("-->")
    try:
        a = int(a)
    except Exception:
        raise UnexceptedInput("wrong type")
    if(not (a - 1) in range(len(mfiles))):
        time.sleep(1)
        raise UnexceptedInput("wrong index")
    return mfiles[a-1]


def expand(fpath, size):
    fpath = str(fpath)
    size = (float(size))  # M
    sizemb = size
    size *= 1024 * 1024  # bytes
    aimbytes = int(size)
    print("%r bytes(%r MB)" % (size, sizemb))
    file = open(fpath, "rb")
    bytesalready = len(file.read())
    file.close()
    if(aimbytes >= bytesalready):
        appendbytes = aimbytes-bytesalready
        temp = bytes(appendbytes)
        file = open(fpath, "ab")
        file.write(temp)
        file.close()
        print(color.generate("\nDone,%r kb was written" % size, color.color.GREEN))
    else:
        print(color.generate("Wrong size!", color.color.RED))


path = input("The path:")
file_name = ""


get_file_name()
mfile = open(path+"/"+file_name, "rb")
msize = len(mfile.read())/1024/1024
mfile.close()
print(color.generate(file_name, color.color.YELLOW))
print("The size is %s" % (msize))
size = input("The size you want to reach(MBit):\n")
if(exists(path)):
    print(color.generate("The path exists.", color.color.GREEN))
    expand((path+"/"+file_name), size)
else:
    print(color.generate("Wrong path!", color.color.RED))
