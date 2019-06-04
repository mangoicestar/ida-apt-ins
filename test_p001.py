#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, pytest
import logging, os, sys, json, configparser, re, traceback, time
import lib.functions

logging.basicConfig(filename="logs/"+str(os.path.basename(sys.argv[0])).split(".py")[0]+".log", format='%(time)s %(module)s.%(funcName)s (%(lineno)d)>>> 	[%(levelname)s] %(message)s', level=logging.INFO)

logging.info("start test ")

#### Define Config properties
config = configparser.ConfigParser()
config.read("config.properties")



@pytest.mark.skipif(eval(config.get('run', 'login'))==False, reason="skip")
def test_login():
	assert lib.functions.getlogin()==0

@pytest.mark.skipif(eval(config.get('run', 'notify'))==False, reason="skip")
def test_notify():
	assert lib.functions.getnotify()==0

@pytest.mark.skipif(eval(config.get('run', 'logout'))==False, reason="skip")
def test_logout():
	assert lib.functions.getlogout()==0

