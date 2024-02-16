#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install opencv-python


# In[5]:


import cv2
color_img = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
cv2.imshow('colorimage',color_img)
cv2.waitKey(0)


# In[5]:


import cv2
image=cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",0)
cv2.imwrite('Cat.jpg',image)


# In[9]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
print(image.shape)


# In[11]:


import cv2
import random
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
for i in range(100):
    for j in range(image.shape[1]):
        image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('part image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
image=cv2.resize(image,(400,400))
tag = image[300:400,300:400]
image[50:150,50:150] = tag
cv2.imshow('partimage1',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
cv2.imshow('Original Image',image)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv)

hsv1 = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv1)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray)

gray1 = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray1)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg")
image = cv2.resize(image,(300,200))

image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('Original HSV Image',image)

RGB = cv2.cvtColor(image,cv2.COLOR_HSV2RGB)
cv2.imshow('2HSV2BGR',RGB)

BGR = cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',BGR)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[7]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg")
image = cv2.resize(image,(300,200))
cv2.imshow('Original RGB Image',image)

YCrCb1 = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)

YCrCb2 = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
cv2.imshow('BGR-2-YCrCb',YCrCb2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[8]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
image = cv2.resize(image,(300,200))

R = image[:,:,2]
G = image[:,:,1]
B = image[:,:,0]

cv2.imshow('R-Channel',R)
cv2.imshow('G-Channel',G)
cv2.imshow('B-Channel',B)

merged = cv2.merge((B,G,R))
cv2.imshow('Merged RGB image',merged)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
image = cv2.resize(image,(300,200))
image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

H,S,V=cv2.split(image)

cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)

merged = cv2.merge((H,S,V))
cv2.imshow('Merged',merged)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:
