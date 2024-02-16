# COLOR_CONVERSIONS_OF-IMAGE
## AIM
To write a python program using OpenCV to do the following image manipulations.

i) Read, display, and write an image.

ii) Access the rows and columns in an image.

iii) Cut and paste a small portion of the image.

iv)To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.


## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg ,
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use imshow(window_name, image) to display the image.
### Step4:
Use imwrite(filename, image) to write the image.
### Step5:
End the program and close the output image windows.
### Step6:
Convert BGR and RGB to HSV and GRAY
### Step7:
Convert HSV to RGB and BGR
### Step8:
Convert RGB and BGR to YCrCb
### Step9:
Split and Merge RGB Image
### Step10:
Split and merge HSV Image

##### Program:
### Developed By : K MADHAVA REDDY
### Register Number: 212223240064


## Output:

### i) Read and display the image
### CODE :
```
import cv2
color_img = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
cv2.imshow('colorimage',color_img)
cv2.waitKey(0)
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/5089931c-37d5-4dd7-b3fc-970ceeae601f)


<br>
<br>

### ii)Write the image
### CODE :
```
import cv2
image=cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",0)
cv2.imwrite('Cat.jpg',image)
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/7a9e264b-7baa-4699-9f59-d69bb8357724)


<br>
<br>

### iii)Shape of the Image
### CODE :
```
import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
print(image.shape)
```
# OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/5ecaba72-8a6f-45bd-b51f-6f04128940f4)

<br>
<br>

### iv)Access rows and columns
### CODE :
```
import cv2
import random
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
for i in range(100):
    for j in range(image.shape[1]):
        image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('part image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/818f6796-cff3-4d4b-bd89-f8ec0de778e4)

<br>
<br>

### v)Cut and paste portion of image
### CODE :
```
import cv2
image = cv2.imread(r"C:\Users\rthir\Downloads\cute cat.jpg",1)
image=cv2.resize(image,(400,400))
tag = image[300:400,300:400]
image[50:150,50:150] = tag
cv2.imshow('partimage1',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/7db028f1-5a96-44f4-8159-d4e64df65541)

<br>
<br>

### vi) BGR and RGB to HSV and GRAY
### CODE :
```
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
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/98447627-42e3-4d10-87d0-57338ebf61b5)

<br>
<br>

### vii) HSV to RGB and BGR
### CODE :
```
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
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/296d474f-1364-4c54-a58e-6d7490754f28)

<br>
<br>

### viii) RGB and BGR to YCrCb
### CODE :
```
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
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/6e735145-6f2e-4af7-9185-8249fad01a39)

<br>
<br>

### ix) Split and merge RGB Image
### CODE :
```
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
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/7535aee0-21d5-484c-bc50-e3284427425b)

<br>
<br>

### x) Split and merge HSV Image
### CODE :
```
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
```
### OUTPUT :
![image](https://github.com/Madhavareddy09/COLOR_CONVERSIONS_OF-IMAGE/assets/145742470/ac6d4cc1-6074-45b3-9df4-e039f02b1c71)

<br>
<br>




## Result:
Thus the images are read, displayed, and written ,and color conversion was performed between RGB, HSV and YCbCr color models successfully using the python program.







