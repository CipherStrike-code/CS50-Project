import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(f"Output:\n{figlet.renderText(text)}")

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in figlet.getFonts():
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(f"Output:\n{figlet.renderText(text)}")
    else:
        print("Invalid Usage")
        sys.exit(1)
else:
    print("Invalid Usage")
    sys.exit(1)
