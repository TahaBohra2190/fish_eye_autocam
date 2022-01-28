# -*- coding: utf-8 -*-
from pickle import STACK_GLOBAL
from types import TracebackType
from configmain import *
warnings.filterwarnings('ignore')

#Function to Show Image and Check if image is Blur
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()

def isblur(image):
  THRESHOLD_BLUR=150
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  fm = variance_of_laplacian(gray)
  if fm < THRESHOLD_BLUR:
    #THRESHOLD_BLUR is below 150 so blur , return 0
    return 0
  else:
    #THRESHOLD_BLUR is above 150,not blur , return 1
    return 1

#Function to check if the captured image is noisy or not
def isnoise(img):
  image=img.copy()
  #convert source image to HSC color mode
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  hsv_low = np.array([0,26,0], np.uint8)
  hsv_high = np.array([255,255,255], np.uint8)
  #making mask for hsv range
  mask = cv2.inRange(hsv, hsv_low, hsv_high)
  median = cv2.medianBlur(mask,5)
  #masking HSV value selected color becomes black
  res = cv2.bitwise_and(image, image, mask=median)
  colour_count = cv2.countNonZero(mask)
  if ( colour_count >12000 and colour_count < 15000) or (colour_count > 20000):
    return 1
  else:
    return 0

#Function to check if the captured image is scrolled or not
def isscrolled(img):
  # Convert image to grayscale
  img_gs = img.copy()
  edges = cv2.Canny(img_gs, 100,200)
  colour_count = cv2.countNonZero(edges)
  if colour_count < 4000:
    return 1
  else:
    return 0

def mse(imageA, imageB):
  err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
  err /= float(imageA.shape[0] * imageA.shape[1])
  return err

#Function to check if the captured image is aligned or not using SSIM - Structural Similarity Index Measure
def isaligned(test_img,perfect_img):
  imageA = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
  imageB = cv2.cvtColor(perfect_img, cv2.COLOR_BGR2GRAY)
  m = mse(imageA, imageB)
  s = ssim(imageA, imageB)
  if m < 10 and s > 0.96:
    return "perfect"
  elif m > 400 and m <750:
    return "inverted"
  elif m<=400 and m >180:
    return "not aligned"
  else:
    return "no issue with alignment"

#Function to check if the captured image is RGB scaled distored or not
def isgray(img):
  if len(img.shape) < 3: return True
  if img.shape[2]  == 1: return True
  b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
  if (b==g).all() and (b==r).all(): return 1
  return 0

def checkscale(img):
  if isgray(img):
    return "Image is in grayscale"
  else:
    w,h,x1 = img.shape
    countb=0
    countg=0
    countr=0
    perfect=0
    for i in range(w):
      for j in range(h):
        rgb = list(img[i, j])
        if rgb[0]>200 and rgb[1]>200 and rgb[2]>200:
          perfect+=1
        elif rgb[0]<200 and rgb[1]<200 and rgb[2]>200:
          countb+=1
        elif rgb[0]<200 and rgb[1]>200 and rgb[2]<200:
          countg+=1
        elif rgb[0]>200 and rgb[1]<200 and rgb[2]<200:
          countr+=1
    if perfect>(w*h*0.8):
      return "Perfect"
    elif countb>(w*h*0.6):
      return "Blue scale"
    elif countg>(w*h*0.6):
      return "Green scale"
    elif countr>(w*h*0.6):
      return "Red scale"
    else:
      return "Image is in RGB scale"

#Function to check if the captured image is mirror image of perfect image or not
def mirror(test_img,perfect_img):
    #why are we flipping?
  perfect_img = cv2.flip(perfect_img, 1)
  score = ssim(test_img, perfect_img, multichannel=True)
  if score>=0.85:
      return 1
  else:
	    return 0
  

#Function to detect and return the number of blackspots
def blackspots(path):
  gray = cv2.imread(path, 0)
# threshold
  th, threshed = cv2.threshold(gray, 100, 255,
  cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
  # findcontours
  cnts = cv2.findContours(threshed, cv2.RETR_LIST,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
  s1 = 8
  s2 = 20
  xcnts = []
  for cnt in cnts:
    if s1<cv2.contourArea(cnt) <s2:
      xcnts.append(cnt)
  return len(xcnts)

#Function to get SSIM - Structural Similarity Index Measure
#The SSIM values ranges between 0 to 1, 1 means perfect match the reconstruct image with original one. 
# Generally SSIM values 0.97, 0.98, 0.99 for good quallty recontruction techniques.
def ssim_score(test_img,perfect_img):
  imageA = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
  imageB = cv2.cvtColor(perfect_img, cv2.COLOR_BGR2GRAY)
  ssimscore = ssim(imageA, imageB)
  return ssimscore



 #Function to get the brisque score - Range 0 is best, 100 is worst
def brisque_score(test_img):
    #img = Image.open(test_img)
    
    #img = img_as_float(io.imread(test_img, as_gray=True))
    #img = img_as_float(io.imread('images/noisy_images/sandstone.tif', as_gray=True))
    brisquescore = brisque.score(test_img)
    return brisquescore
    #print("this except of Brisque code")