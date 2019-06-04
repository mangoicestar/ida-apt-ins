#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, pytest
import os, sys, logging, json

logging.basicConfig(filename="logs/"+str(os.path.basename(sys.argv[0])).split(".py")[0]+".log", format='%(asctime)s %(module)s.%(funcName)s (%(lineno)d)>>> 	[%(levelname)s] %(message)s', level=logging.INFO)

logging.info("start test ")


def getlogin():
	login=0
	logging.info("login  = " + str(login))
	return login

def getnotify():
	notify=0
	logging.info("notify = " + str(notify))
	return notify

def getlogout():
	logout=0
	logging.info("logout =" + str(logout))
	return logout

