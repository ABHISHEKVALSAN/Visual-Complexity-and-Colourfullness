import subprocess
import sys
import numpy as np
import webcolors
import re
import string
import sys
import unidecode
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from itertools import groupby
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
def saveScreenshot(driver,url):
	imgName=url.split('//')[1].split('/')[0]
	driver.save_screenshot('/home/abhiavk/git/Visual-Complexity-and-Colourfullness/Training/IndiaGov/'+imgName+'.png')
def main(filename):
	options 	= Options()
	options.add_argument("--headless")
	driver		= webdriver.Chrome(chrome_options=options)
	driver.set_window_size(1024,768)
	urls		=open(filename,"r")
	for url in urls:
		url=url[:-1]
		print(url)
		driver.get(url)
		saveScreenshot(driver,url)
	driver.quit()
if __name__=="__main__":
	filename=sys.argv[-1]
	main(filename)
