#!/usr/bin/env python
# encoding: utf-8
"""
import_imgs.py

Created by Kim Pettersen on 2012-07-15.
Copyright (c) 2012 kim.a.pettersen@gmail.com. All rights reserved.
"""

import sys
import os
import pymongo

def main():
	path = '/Users/kim/dev_repositories/weather_learner/learner_app/learner_app/static'
	c = 0
	paths = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith('.jpeg'):
				c += 1
				path = root + '/' + name
				path = path.split('/static/')[1]
				paths.append(path)
	import_image_paths(paths)

def import_image_paths(paths):
	for path in paths:
		db.paths.insert({
			'path' : path,
			'label': ''
			})
	print len(paths)

if __name__ == '__main__':
	c = pymongo.Connection()
	db = c.imgs
	main()

