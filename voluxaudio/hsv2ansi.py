# function by Denver P. 2019
from colorama import init
init()
from colorama import Fore, Back, Style

def hsv2ansi(h,s,v):
    ansi = None
    red_to_yellow = 45/360
    # yellow_to_green = 150/360 # more accurate to reality, doesn't quite match lights
    yellow_to_green = 100/360
    green_to_cyan = 195/360
    cyan_to_blue = 225/360
    blue_to_magenta = 285/360
    magenta_to_red = 345/360

    # get colour based on hue
    if (h>=magenta_to_red or h<red_to_yellow):
        ansi_fore = Fore.RED
        ansi_back = Back.RED
    elif (h>=red_to_yellow and h<yellow_to_green):
        ansi_fore = Fore.YELLOW
        ansi_back = Back.YELLOW
    elif (h>=yellow_to_green and h<green_to_cyan):
        ansi_fore = Fore.GREEN
        ansi_back = Back.GREEN
    elif (h>=green_to_cyan and h<cyan_to_blue):
        ansi_fore = Fore.CYAN
        ansi_back = Back.CYAN
    elif (h>=cyan_to_blue and h<blue_to_magenta):
        ansi_fore = Fore.BLUE
        ansi_back = Back.BLUE
    elif (h>=blue_to_magenta and h<magenta_to_red):
        ansi_fore = Fore.MAGENTA
        ansi_back = Back.MAGENTA
    else:
        print("I DUNNO! D:")
        raise Exception("color doesn't fit any conditions!")

    return(ansi_fore,ansi_back)

def demo():
    for i in range(360):
        ansi = hsv2ansi(i/360,0,0)
        print("{}° = {}demo{}".format(i,ansi[0],Style.RESET_ALL))

if __name__ == '__main__':
    demo()
