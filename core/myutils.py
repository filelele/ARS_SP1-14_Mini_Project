import cv2

def crop_and_resize(frame):
    padding = int((frame.shape[1]-frame.shape[0])/2)
    frame_cut_to_square = frame[:, padding+120: padding + frame.shape[0] + 120, :]
    frame_cut_and_resize = cv2.resize(frame_cut_to_square, (224, 224), interpolation=cv2.INTER_CUBIC)
    frame_final = cv2.cvtColor(frame_cut_and_resize, cv2.COLOR_BGR2RGB)
    x_pixels_pad = padding + 120

    return frame_final, x_pixels_pad

def topLeftBottomRight(xmin_ratio, ymin_ratio, w_ratio, h_ratio, xpadding, origin_small_side):
    # Calculate top left and bottom right points of bounding box using center coordinates
    xmin = xmin_ratio * origin_small_side + xpadding
    ymin = ymin_ratio * origin_small_side
    w = w_ratio * origin_small_side
    h = h_ratio * origin_small_side

    top_left = (int(xmin), int(ymin))
    bottom_right = (int(xmin + w), int(ymin + h))

    return top_left, bottom_right