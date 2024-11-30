# Problem

### Introduction
Currently, many manufacturing factories need to automate product 
counting and identification, such as: 
- Production lines in the factory
- Product classification/packaging lines of logistics companies 
- The process of importing/exporting warehouses, buying and selling 
products of supermarkets, etc.

![image](https://github.com/user-attachments/assets/6caf3b11-c99c-4a7f-ad7f-0cade4a99972)

### Problem description

![image](https://github.com/user-attachments/assets/f8957468-76b1-4c4e-a982-1f03253adad8)

Figure shows a simple conveyor system, consisting of the following 
components: 
- Conveyor belt
- The camera is fixed above, looking down at the conveyor belt.
- Objects are confectionery products. 

The following data will be provided for investigation: 
- Image data of the objects
- Video data (video files) of objects moving on the conveyor belt.

Sharepoint link for raw_data: 

`https://husteduvn-my.sharepoint.com/:u:/g/personal/phi_lh213633_sis_hust_edu_vn/ES1US0ilXJdAsMr6MP_4xO4BVKTEmQzpGABsP5ojIPVETA?e=B2OfOn`

### Goal
 
- Classify objects moving on the conveyor belt
- Count the number of each class
- Display results on screen

# Solution Overview
### Diagram
![image](https://github.com/user-attachments/assets/00d8a268-6601-47e8-bc63-87f5986c4a8c)

### Classification
Resnet 50 pretrained is used since the ImageNet and the objects to classify in this problem have high similarity (box shape, common product, ...)

***Some preprocessings on raw data***

1. Frames size
 
ImageNet dataset is of the size 224x224, but our video frames are in different shape:
- 1536x2048 for conveyor belt video frames.
- 1280x720 for objects capturing from phone.

Eventhough Resnet accept varying image shape, utilizing pretrained weights require the input to the model to be exactly 224x224 as ConvBlock will have different receptive field on different image sizes.

A simple way to convert frames to desired 224x224 is given below:

![image](https://github.com/user-attachments/assets/58e0d0a3-5960-4221-a081-95cbdd03581c)

Sharepoint link for 224x224 cropped out frames: 

`https://husteduvn-my.sharepoint.com/:u:/g/personal/phi_lh213633_sis_hust_edu_vn/EcJBKOrco-hEqANPfyfqQfMBzjUKwwcxZQgwCLRQAWHs7Q?e=xnx3CG`

2. Noise data

- Frames with just a part of the object are considered noise data, as it misguides the model to stick irrelevant features to labelled class.
Such frames are removed from the dataset

![image](https://github.com/user-attachments/assets/ddea4cc1-2394-4d44-b779-7b7a0a95f8c3)

3. Data imabalance

- The huge amount of "background" data samples comparing to other classes make the dataset imbalance, so part of its data samples is removed.

- The effect of data imbalance between classes can also be reduced by using "Class weights", a way to balance the contribution to total loss of classes with different number of data samples.

![image](https://github.com/user-attachments/assets/e922c8d4-b750-4eaa-83c3-06601865577c)

### Bounding box

Currently using simple HSV to remove green color of conveyor belt from the frame to get the object, but this way is unreliable as color of some products is unwantedly removed.
The mentor recommended me to use Background subtraction as a more robust way in this kind of problem, I have not implemented it yet.

# Final results
Time constraint did not allow me to do a proper measurement as I was busy fixing the model. This solution is finished at the last minutes just before the presentation time.
Before that I did try many other ways and failed wasting a lot of time. The test result on the video test is given below:

[![image](https://github.com/user-attachments/assets/eed6c603-1e8a-4b30-80e5-313f0ccad453)](https://husteduvn-my.sharepoint.com/:v:/g/personal/phi_lh213633_sis_hust_edu_vn/EdHxjMRWdk5CtwyoYqcvBWsBdMNasIxNE8vOoReozo02Ww?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=gju3Jg)

# END

