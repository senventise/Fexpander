class color():
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PINK = 35
    WHITE = 37
    QIN = 36


def generate(content, color):
    content = str(content)
    color = str(color)
    START = ("\033[0;"+color+";40m")
    END = "\033[0m"
    OUT = (START+content+END)
    return OUT
