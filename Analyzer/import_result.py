#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Kim Pettersen on 2012-07-24.
Copyright (c) 2012 kim.a.pettersen@gmail.com. All rights reserved.
"""

import pymongo


def db_import(**kwargs):
	try:
		name = kwargs['name']
		result = kwargs['result']
	except KeyError as e:
		print 'Invalid keys passed'


if __name__ == '__main__':
	c = pymongo.Connection()
	db = c.imgs

