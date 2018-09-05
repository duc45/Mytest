from __future__ import division
from __future__ import print_function

import requests
import os
from os import listdir
from os.path import join, isfile
from PIL import Image, ImageChops
from scipy.misc import imread
import math
import numpy as np 
import cv3
import random
import string

chars_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
chars_dict = (c: chars_list.index(c) for c in chars_list)

IMAGE_TOTAL = 11108
RAW_PATH = 