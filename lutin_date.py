#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import datetime

def get_type():
	return "LIBRARY_STATIC"

def get_desc():
	return "Date buid date of the program"

def get_licence():
	return "MPL-2"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "atria-soft"

def get_maintainer():
	return "authors.txt"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.add_src_file([
	    'date/date.cpp'
	    ])
	my_module.add_header_file([
	    'date/date.hpp'
	    ])
	now = datetime.datetime.now()
	my_module.add_flag('c++', [
	    '-Wno-write-strings',
	    '-Wall',
	    "-DBUILD_DAY=\""+str(now.day)+"\"",
	    "-DBUILD_MONTH=\""+str(now.month)+"\"",
	    "-DBUILD_YEAR=\""+str(now.year)+"\"",
	    "-DBUILD_HOUR=\""+str(now.hour)+"\"",
	    "-DBUILD_MINUTE=\""+str(now.minute)+"\"",
	    "-DBUILD_SECOND=\""+str(now.second)+"\""
	    ])
	return True


