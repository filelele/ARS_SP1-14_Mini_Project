import cv2
import numpy as np

lower_green = np.array([90/2,1*2.55,1*2.55])  # Low saturation and brightness for green
upper_green = np.array([165/2,100*2.55,100*2.55])

lower_white = np.array([25/2,0*2.55,25*2.55])  # High brightness for white
upper_white = np.array([80/2,50*2.55,50*2.55])

def getBbox(image):
    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create masks for green and white part of background
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_white = cv2.inRange(hsv, lower_white, upper_white)

    # Combine masks
    background_mask = cv2.bitwise_or(mask_green, mask_white)

    # Invert mask to get the object
    object_mask = cv2.bitwise_not(background_mask)

    # Apply morphological operations to clean up noise
    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    clean_mask = cv2.morphologyEx(object_mask, cv2.MORPH_OPEN, kernel_open)
    kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, kernel_close)

    # Find contours in the mask
    contours, _ = cv2.findContours(clean_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Select the largest contour (assuming it's the object of interest)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)

        # Get bounding box for the largest contour
        xmin, ymin, w, h = cv2.boundingRect(largest_contour)

    return xmin, ymin, w, h

def minpointToCenter(xmin, ymin, w, h):
    # Calculate center of bounding box
    xcenter = xmin + w/2
    ycenter = ymin + h/2

    return xcenter, ycenter, w, h

def topLeftBottomRight(xmin_ratio, ymin_ratio, w_ratio, h_ratio, xpadding, origin_small_side):
    # Calculate top left and bottom right points of bounding box
    xmin = xmin_ratio * origin_small_side + xpadding
    ymin = ymin_ratio * origin_small_side
    w = w_ratio * origin_small_side
    h = h_ratio * origin_small_side

    top_left = (int(xmin), int(ymin))
    bottom_right = (int(xmin + w), int(ymin + h))

    return top_left, bottom_right