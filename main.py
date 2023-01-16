
from PIL import Image
import numpy as np

print("Loading Images")

# load the two input images
# image1 = io.imread("./Images/orig_image.jpg")
# image2 = io.imread("./Images/sd_image.jpg")

image1 = Image.open("./Images/orig_image.jpg")
image2 = Image.open("./Images/sd_image.jpg")



print("Images loaded")

# check that the images have the same shape
assert image1.size == image2.size, "Error: Images must have the same shape"

print(image1.size)
print(image2.size)


pixel_values_image1 = np.array(list(image1.getdata()))
pixel_values_image2 = np.array(list(image2.getdata()))

print(pixel_values_image1)
print(pixel_values_image2)

pix_values = pixel_values_image2 - pixel_values_image1

print(len(pix_values))

array = np.array(pix_values, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save('./Images/result.png')









# print("Calculating....")

# result = image1 - image2

# print("Result calculated")

# # save the result
# io.imsave("result.png", result)

# print("Image saved")

# fig, ax = plt.subplots(nrow=1, ncols=3)

# # plot the original images
# ax[0].imshow(image1)
# ax[0].set_title("Original Image 1")
# ax[1].imshow(image2)
# ax[1].set_title("SD Image")

# # Plot the resulting image as a heatmap
# ax[2].imshow(result, cmap="jet")
# ax[2].set_title("Resulting Image")