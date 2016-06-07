#!/usr/bin/env python2.7
import argparse
import os

def parse_args():
	parser=argparse.ArgumentParser(description='disaply a tree like structure for a given dir')
	parser.add_argument(dest='path', metavar='directory')
	return parser.parse_args()

def get_dirlist(path):
	dirlist=os.listdir(path)
	dirlist.sort()
	return dirlist

def print_files(path, prefix= ""):
	if prefix=="":
		print("Directory Listings for : "+path)
		prefix="| "

	dirlist=get_dirlist(path)
	for f in dirlist:
		full_name=os.path.join(path, f)
		if os.path.isdir(full_name):
			print_files(full_name, prefix + "| ")
			print (prefix + "+ " + f) # display a dir with "+" in the front
		else:
			print (prefix + f)

def main():
	path = "/py/proj/tree/testdir"
	#args=parse_args()
	#path = args.path
	print_files(path)

if __name__ == "__main__":
	main()
