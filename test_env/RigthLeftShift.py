import cv2
import TM_fisheye_image as tmf

sample_image = cv2.imread("images\Master_image_.png",cv2.IMREAD_COLOR)


def Shift_detection(test_image):
    shift_direction = [0 ,0 ,0 ,0]
    top_left , bottom_right = tmf.extract_target(test_image)
    if (top_left[0] > 551 and  bottom_right[0] > 1432):shift_direction[0] = 1
    elif (top_left[0] < 551 and  bottom_right[0] < 1432):shift_direction[1] = 1
    elif (top_left[1] < 151 and  bottom_right[1] < 987):shift_direction[2] = 1
    elif (top_left[1] > 151 and  bottom_right[1] > 987):shift_direction[3] = 1

    return shift_direction

print(Shift_detection(sample_image))