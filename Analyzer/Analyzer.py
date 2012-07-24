#!/usr/bin/env python
# encoding: utf-8
"""
Analyzer.py

Created by Kim Pettersen on 2012-07-17.
Copyright (c) 2012 kim.a.pettersen@gmail.com. All rights reserved.
"""

import sys
import os
import pymongo
from PIL import Image

abs_path = '/Users/kim/dev_repositories/weather_learner/learner_app/learner_app/static/'
analysis_path = '/Users/kim/dev_repositories/weather_learner/Analyzer/analysis'
thumb_size = 128, 128
enabled_analysis = ['sasturation']

analysis_dir = str(os.getcwd()) + '/analysis'
os.sys.path.insert(0, analysis_dir)

def main():
	entry = db.paths.find_one( { 'label': { '$ne' : ''} } )
	path = abs_path + entry['path']
	image = get_image(path=path)
	analyze(image=image)
	
def get_image(**kwargs):
	try:
		path = kwargs['path']
	except KeyError as e:
		print 'KeyError: ' + str(e.args[0]) + ' not passed'
		exit()

	img = Image.open(path)
	thumb = img.copy()
	thumb.thumbnail(thumb_size, Image.ANTIALIAS)
	return thumb
	
def analyze(**kwargs):
	try:
		image = kwargs['image']
	except KeyError as e:
		print 'KeyError: ' + str(e.args[0]) + ' not passed'
		exit()
	try:
		modules = map(__import__, enabled_analysis)		
	except ImportError as e:
		print 'Import error: ' + str(e.args[0])
		print 'Analyzer will exit..'
		exit()
		
	for module in modules:
		try:
			module.run(image=image)
		except Exception as e:
			print type(e)
			print 'Error running analysis: ' + str(module)
			
if __name__ == '__main__':
	c = pymongo.Connection()
	db = c.imgs
	main()

