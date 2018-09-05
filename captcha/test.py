import random
import os

FONT_PATH = '/tensorflow/captcha/generate_captcha/font'

list_font = os.listdir(FONT_PATH)
rndFont = random.choice(list_font)
print(FONT_PATH + "/" + rndFont)
