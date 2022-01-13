import cv2
#importing the template matching function to return the co-ordinates of the template match 
import TM_fisheye_image as tmf

sample_image = cv2.imread("images\\rawimage3.png",cv2.IMREAD_COLOR)


def Shift_detection(test_image):
    # The 4 indices of the array represent the different directions of shift in the order Rigth , Left , Top , Bottom 
    shift_direction = [0 ,0 ,0 ,0]
    top_left , bottom_right = tmf.extract_target(test_image)
    if (top_left[0] > 551 and  bottom_right[0] > 1432):shift_direction[0] = 1
    elif (top_left[0] < 551 and  bottom_right[0] < 1432):shift_direction[1] = 1
    elif (top_left[1] < 151 and  bottom_right[1] < 987):shift_direction[2] = 1
    elif (top_left[1] > 151 and  bottom_right[1] > 987):shift_direction[3] = 1

    return shift_direction

print(Shift_detection(sample_image))