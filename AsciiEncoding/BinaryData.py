with open("AccessData Registry Viewer_1.8.3.exe", "rb") as f:
    data = f.read()
    print data.encode("base64")