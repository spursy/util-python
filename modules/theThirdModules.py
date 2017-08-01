#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# pip is the modules management.

# import path is from sys.path
import sys
print(sys.path)

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)