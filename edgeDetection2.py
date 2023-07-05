import cv2 
import matplotlib.pyplot as plt
# importing the image.
img = cv2.imread("azadChaiwala.jpg")
# making edges (picture)
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)

plt.figure()
plt.title("Guess him!")
plt.imsave("azadChaiwala.png", edges, cmap="gray", format= "png")
plt.imshow(edges, cmap="gray")
plt.show()


