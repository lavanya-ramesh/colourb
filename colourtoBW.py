from PIL import Image
img=Image.open(r'C:\Users\lava0\OneDrive\Pictures\passport image.jpg');
bw=img.convert("L")
bw.show()
