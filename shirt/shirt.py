import os
import sys
from PIL import Image, ImageOps

def main():
    argument_num()
    try:
        '''
        muppet = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        muppet = ImageOps.fit(muppet,size)
        muppet.paste(shirt,shirt)
        muppet.save(sys.argv[2])
        sys.exit(0)
        '''
        muppet = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = muppet.size
        shirt = ImageOps.fit(shirt,size)
        muppet.paste(shirt,shirt)
        muppet.save(sys.argv[2])
        sys.exit(0)

    except FileNotFoundError:
        sys.exit("File not found")

def argument_num():
    if len(sys.argv) == 3:
        argv1 = os.path.splitext(sys.argv[1])
        argv2 = os.path.splitext(sys.argv[2])
        ext = ['.jpeg','.jpg','.png']
        if argv1[1] and argv2[1] in ext:
            if argv1[1] == argv2[1]:
                pass
            else:
                sys.exit("Input and output have different extensions")
        elif argv2 not in ext:
            sys.exit("Invalid Output")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()