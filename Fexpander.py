import os
import sys
import color
import time
from os.path import exists
from dirTest import file_name as fn


def choose_file(mpath):
    try:
        mfiles = fn(mpath)
    except FileNotFoundError:
        print(color.generate("Wrong path!", color.color.RED))
        sys.exit(0)
    for index, item in enumerate(mfiles):
        print(str(index+1)+"\t"+item)
    print(color.generate("\nplease input the index", color.color.YELLOW))
    a = input("-->")
    try:
        int(a)
    except ValueError:
        print(color.generate("please input the index, not the file name!", color.color.RED))
    if(not (a - 1) in range(len(mfiles))):
        print(color.generate("Error index!", color.color.RED))
        time.sleep(1)
        choose_file(mpath)
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
        print(color.generate("%r MB was written" % size, color.color.GREEN))
    else:
        print(color.generate("Wrong size!", color.color.RED))


path = input("The path:")
file_name = choose_file(path)
mfile = open(path+"/"+file_name, "rb")
msize = len(mfile.read())/1024/1024
mfile.close()
print(color.generate(file_name, color.color.YELLOW))
print("The size is %s" % (msize))
size = input("The size you want to reach(MBit):\n")
if(exists(path)):
    print(color.generate("The path exists.", color.color.GREEN))
    expand((path+"/"+name), size)
else:
    print(color.generate("Wrong path!", color.color.RED))

