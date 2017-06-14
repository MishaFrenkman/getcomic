#!/usr/bin/python

import requests
import envoy
from random import randint
from bs4 import BeautifulSoup
from urllib import urlretrieve
import time

number = randint(1, 1850)

r = requests.get("https://xkcd.com/%d/" %number)
src = "https:" + BeautifulSoup(r.text, "lxml").find(id="comic").find("img")["src"]

urlretrieve(src, "pic.png")
envoy.run("open pic.png")

#time.sleep(1)
#envoy.run("rm pic.png")