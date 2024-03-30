def convert(emoticons):
    emoji = emoticons.replace(":)","🙂")
    emoji = emoji.replace(":(","🙁")
    return emoji

def main():
    text = input("Input a sentence: ")
    text = convert(text)
    print(text)

main()
