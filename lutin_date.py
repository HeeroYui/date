#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import datetime

def get_type():
	return "LIBRARY"

def get_desc():
	return "Date buid date of the program"

def get_licence():
	return "APACHE-2"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "atria-soft"

def get_maintainer():
	return ["Mr DUPIN Edouard <yui.heero@gmail.com>"]

def get_version():
	return [0,2,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		'date/date.cpp'
		])
	my_module.add_header_file([
		'date/date.h'
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
		"-DBUILD_SECOND=\""+str(now.second)+"\""])
	my_module.add_path(tools.get_current_path(__file__))
	return my_module


