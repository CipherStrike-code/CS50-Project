def main():
    output = input("File name: ").strip().lower()
    print(extensions(output))

def extensions(x):
    if x[-4:] == ".gif":
        return "image/gif"
    elif x[-4:] == ".jpg" or x[-5:] == ".jpeg":
        return "image/jpeg"
    elif x[-4:] == ".png":
        return "image/png"
    elif x[-4:] == ".pdf":
        return "application/pdf"
    elif x[-4:] == ".txt":
        return "text/plain"
    elif x[-4:] == ".zip":
        return "application/zip"
    else:
        return "application/octet-stream"

main()
