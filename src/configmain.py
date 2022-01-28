# -*- coding: utf-8 -*-
#used for relative path calculation
import os
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import pathlib
import warnings
import csv
#this import are for brisque
from skimage import io, img_as_float
import imquality.brisque as brisque
import traceback

#global_path = "C:/Users/admin/Documents/Dashboard_Camera_Testing"
#global_path = "C:/Users/arun_/Downloads/CanProjects/AutomatedCamera/AutomatedCamera/autocamera"
#global_path = "C:/Users/arun_/Downloads/CanProjects/AutomatedCamera/AutomatedCameraArun"


#global_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
BASE_PATH = pathlib.Path(__file__).parents[1]
#BASE_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
#print(global_path)

"""Reading data from config.ini file"""
"""Load configuration from .ini file."""
""" import configparser
# Read local `config.ini` file.
Config = configparser.ConfigParser()
Config.read('config.ini')

# Get values from our .ini file
Config.get('perfectimagepath', 'testimagespath','testresultspath')
Config['perfectimagepath'],['testimagespath'],['testresultspath']


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1 """