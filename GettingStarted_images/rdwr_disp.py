import numpy as np
import cv2

# Load a color image in grayscale
imgloc = 'dog.png'
img_color = cv2.imread(imgloc, cv2.IMREAD_COLOR)
img_gray = cv2.imread(imgloc, cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread(imgloc, cv2.IMREAD_UNCHANGED)

# Display the images
print img_color
cv2.imshow('color', img_color)
print img_gray
cv2.imshow('gray', img_gray)
print img_unchanged
cv2.imshow('unchanged', img_unchanged)

key = cv2.waitKey(0) # wait indefinitely for a keystroke
    
while key != 27:
    if key == ord('c'): # wait for 'c' key to save color image and exit
        cv2.imwrite('dog_color.png', img_color)
        cv2.destroyAllWindows() # close all windows
        break
    elif key == ord('g'): # wait for 'g' key to save gray image and exit
        cv2.imwrite('dog_gray.png', img_gray)
        cv2.destroyAllWindows() # close all windows
        break
    key = cv2.waitKey(0) # continue waiting

cv2.destroyAllWindows() # close all windows

# cv2.destroyWindow('<window name>') # destroys specific window