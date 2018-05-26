class color():
    class way():
        NULL=0
        HIGHLIGHT=1
        UNDERLINE=4
        BLINK=5
    class back():
        BLACK=40
        RED=41
        GREEN=42
        YELLOW=43
        BLUE=44
        PINK=45
        WHITE=47
        QIN=46
    class front():
        BLACK=30
        RED=31
        GREEN=32
        YELLOW=33
        BLUE=34
        PINK=35
        WHITE=37
        QIN=36

def Crint(content,way,fcolor,bcolor):
    #@content:the text you want print
    #@bcolor: background color
    #@fcolor:front color
    #@way:the way you want to print
    content=str(content)
    bcolor=str(bcolor)
    fcolor=str(fcolor)
    way=str(way)
    START=("\033["+way+";"+fcolor+";"+bcolor+"m")
    END="\033[0m"
    OUT=(START+content+END)
    print(OUT)

#test
#Crint("Hello.",color.way.NULL,color.front.BLACK,color.back.WHITE)

