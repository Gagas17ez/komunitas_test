import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
  
fig = plt.figure(figsize=(10, 7))
  
rows = 2
columns = 2
  
Image1 = mpimg.imread('image1.jpg')
Image2 = mpimg.imread('image2.png')
Image3 = mpimg.imread('image3.png')
Image4 = mpimg.imread('image4.png')
  
fig.add_subplot(rows, columns, 1)
  
plt.imshow(Image1)
plt.axis('off')
plt.title("First")

fig.add_subplot(rows, columns, 2)
  
plt.imshow(Image2)
plt.axis('off')
plt.title("Second")
  
fig.add_subplot(rows, columns, 3)
  
plt.imshow(Image3)
plt.axis('off')
plt.title("Third")
  
fig.add_subplot(rows, columns, 4)
  
plt.imshow(Image4)
plt.axis('off')
plt.title("Fourth")

plt.show()