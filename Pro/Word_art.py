import termcolor
import  pyfiglet

word = input("What would you like to print? ")
c = input("Which color? ").lower()

valid_colors = ("red","green","yellow","blue","magenta","cyan","black")

if c not in valid_colors:
    c = "magenta"

art = pyfiglet.figlet_format(word)
color_art = termcolor.colored(art, color=c)
print(color_art)