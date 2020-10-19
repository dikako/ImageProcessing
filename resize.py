#Import required Image library
from PIL import Image

#Create an Image Object from an Image
im = Image.open("image/image.jpeg")

#Display actual image
print("Image Format: " + im.format)

print("Image Mode Color: " + im.mode)

print("Image Size: " + im.size)

# im.show()

#Make the new image half the width and half the height of the original image
resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))

resized_im = im.resize((500,500))

#Display the resized imaged
# resized_im.show()

print(resized_im.size)

#Save the cropped image
resized_im.save('image_canges/image_canges.jpeg')