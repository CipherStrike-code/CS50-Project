def main():
    ans = input("File Type: ").strip().lower()
    ext(ans)

def ext(x):
    if x[-4:] == ".gif" or x[-4:] == ".png":
        print(f"image/{x[-3:]}")
    elif x[-4:] == ".jpg" or x[-5:] == ".jpeg":
        print("image/jpeg")
    elif x[-4:] == ".pdf" or x[-4:] == ".zip":
        print(f"application/{x[-3:]}")
    elif x[-4:] == ".txt":
        print("text/plain")
    else:
        print("application/octet-stream")

main()










