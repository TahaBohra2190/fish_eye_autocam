"""
DISCLAIMER : In order to achieve an output user needs to alter values for 3 variables
            1) In line 14 for the object named sample_image alter the path to master image for your device
            2) In line 21 for the object named template alter the path to template image for your device
            3) In line 83 for the imwrite function alter the path to extracted image for your device
"""

"""
This script will take the raw image from the fisheye camera as input and gives a cropped out image of only the square in the center
It takes the image captured in the main file and uses template matching to find the position of the central square in master  image .
"""
import cv2

#Reading the master image (hardcoded for now)
sample_image = cv2.imread("images\Master_image_inverted.png",cv2.IMREAD_COLOR)

#funtion to extract the square from master image
def extract_target(sample_image):
  source = sample_image
  #importing the template
  template = cv2.imread("images\\rawimage5_template.png")

  #display the image preview, the image_resized variable is used to resize the image into a viewable window of smaller size 
  image_resized = cv2.resize(source, (1280,720))
  cv2.imshow('Preview', image_resized) 
  cv2.waitKey(0) 

  #converting to grayscale to make template matching easy 
  #the cvtColor function used to convert from RGB to greyscale takes 2 parameters as input, 
  # 1) object to apply color change
  # 2)the color space conversion code 
  source = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
  template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY) 

  #Preview image in greyscale
  image_resized = cv2.resize(source, (1280,720))
  cv2.imshow('Preview Greyscaled', image_resized)
  cv2.waitKey(0)  

  #capturing the height and width of master image using default .shape method
  height, width , channelss = source.shape

  #capturing the height and width of template using default .shape method
  H, W , C = template.shape

  #a list of all the methods to see results from all the methods 
  # methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
  #for now we are only using the squared differential method  
  method_s = [cv2.TM_SQDIFF ]

  #this loop runs for every variable in the method list containing names of every variable to use
  for method in method_s:
    src2 = source.copy()
    #OpenCV funtion for template matching, takes 3 inputs 
    # 1) Image to search for template in 
    # 2) Image to use as a template
    # 3) Method to use for template matching 
    result = cv2.matchTemplate(src2, template, method)
    #minMaxLoc goes through the matrix and find the minimum and the maximum value. Note that the input image has to be grayscale.
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

  # Using the values in the 
  x_diff = 551-min_loc[0]
  y_diff = 151-min_loc[1]
  print("Offset")
  print("X : "+str(x_diff))
  print("Y : "+str(y_diff))

  region_of_interest = source[ location[1] : location[1] + W , location[0] : location[0] + H  ]
  # Writing the Area detected in the square detected into an image at the path specified in the first varaible in imwrite function
  cv2.imwrite("images\Cropped_master.png",region_of_interest)
  #the function returns the co-ordinates for the Top left and the bottom right of the square 
  return(location,bottom_right)

extract_target(sample_image)











