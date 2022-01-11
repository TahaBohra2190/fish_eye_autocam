import cv2
import TM_fisheye_image as tmf

sample_image = cv2.imread("images\Master_image_inverted.png",cv2.IMREAD_COLOR)


def Allignment_detection(test_image):
    is_alligned = 1
    top_left , bottom_right = tmf.extract_target(test_image)
    if (top_left[0] > 551 and  bottom_right[0] > 1432):is_alligned = 0
    elif (top_left[0] < 551 and  bottom_right[0] < 1432):is_alligned = 0
    elif (top_left[1] < 151 and  bottom_right[1] < 987):is_alligned = 0
    elif (top_left[1] > 151 and  bottom_right[1] > 987):is_alligned = 0

    return is_alligned

print(Allignment_detection(sample_image))