import base64

def base64_to_image(base64_data, output_path):


    image_data = base64.b64decode(base64_data)
    with open(output_path, "wb") as image_file:
        image_file.write(image_data)
 


with open("test.txt","r") as file:
    rea = file.read()




base64_encoded_image = '"' + rea + '"' # 替换为实际的Base64编码
output_path = "output_image.jpg"  # 替换为输出图片的路径和文件名
 
base64_to_image(base64_encoded_image, output_path)
print("Image saved:", output_path)