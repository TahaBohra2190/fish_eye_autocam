"""
This script is meant to check test an image for allignment
It takes the image captured in the main file and uses template matching to find the position of the symbol in target image 1.
Th escript will check for allignment by cheking the variance between the position of target symbol between the original image and the camera capture.
The threshhold is set to 5 pixels lengthwise and width wise. 
"""
import cv2

sample_image = cv2.imread("images\Master_image_inverted.png",cv2.IMREAD_COLOR)
def extract_target(sample_image):
  source = sample_image
  template = cv2.imread("images\\rawimage5_template.png")

  #display the image preview
  #the imshow function takes two inputs, the name of the window and the object to display from
  image_resized = cv2.resize(source, (1280,720))
  cv2.imshow('Preview', image_resized) 
  cv2.waitKey(0) 

  #converting to grayscale to make template matching easy 
  #the cvtColor function used to convert from RGB to greyscale takes 2 parameters as input, 
  # 1) object to apply color change
  # 2)the color space conversion code 
  # source = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
  # template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY) 

  #Preview image in greyscale
  image_resized = cv2.resize(source, (1280,720))
  cv2.imshow('Preview Greyscaled', image_resized)
  cv2.waitKey(0)  

  #capturing the height and width
  height, width , channelss = source.shape

  H, W , C = template.shape

  #a list of all the methods to see results from all the methods
  # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
  method_sq = [cv2.TM_SQDIFF ]

  #main loop
  for method in method_sq:
    #this loop goes through all the methods of template matching and produces a result for all of them
    src2 = source.copy()
    result = cv2.matchTemplate(src2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("Found at cordinates" + str(min_loc))
    if method in [cv2.TM_SQDIFF,cv2.TM_CCORR]:
      location = min_loc
    else:
      location = max_loc
    
    bottom_right = (location[0] + W, location[1] + H)
    cv2.rectangle(src2, location,bottom_right, [255,255,255], 5)
    image_resized = cv2.resize(src2, (1280,720))
    cv2.imshow('Template matched',image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

  x_diff = 551-min_loc[0]
  y_diff = 151-min_loc[1]
  print("Offset")
  print("X : "+str(x_diff))
  print("Y : "+str(y_diff))

  #need to patch the invert bug
  region_of_interest = source[ location[1] : location[1] + W , location[0] : location[0] + H  ]
  cv2.imwrite("images\Cropped_master.png",region_of_interest)

extract_target(sample_image)




# #capturing the height and width
# height, width =source.shape
# height, width 

# H, W = template.shape
# H, W 

# #a list of all the methods to see results from all the methods
# # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# method_sq = [cv2.TM_SQDIFF]



# x_diff = 269-min_loc[0]
# y_diff = 177-min_loc[1]
# if min_loc == (269,183):
#     print("image is alligned")
# else:
#     print("Not alligned")
# print(location)


