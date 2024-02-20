import base64

point = input()


with open(point, "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(b64_string.decode('utf-8'))

with open("test.txt","w") as f:
        f.truncate
        f.write(b64_string.decode('utf-8'))
