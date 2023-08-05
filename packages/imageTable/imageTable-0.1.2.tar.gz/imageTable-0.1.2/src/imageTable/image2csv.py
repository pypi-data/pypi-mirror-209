#!/usr/bin/env python3

import os
import sys
import argparse
import h5py
import numpy as np
import datatable as dt
import czifile as zis
from pathlib import Path
import flowkit as fk
import pandas as pd
import imageTable
#exec(open("/Users/kevin/Desktop/pixelTable/src/pixelTable/pixelTable.py").read())

class ArgumentParserError(Exception):
	pass

class NewArgumentParser(argparse.ArgumentParser):
	def error(self, message):
		print(message)
		sys.exit(0)


def parse_args(args):
	p = NewArgumentParser(description='convert an ims file to a csv file')
	a = p.add_argument_group('data loading parameters')
	a.add_argument('filename',
					help='File path of input data ims file.')
	a.add_argument('-o', '--output_file', metavar='O', required=False, default = None,
					help='File path of the output csv file. default: a file saved to the present working directory where the .ims extension is replaced by .csv')
	try:
		return p.parse_args(args)
	except ArgumentParserError:
		raise


def main(args: list = None):
	args = parse_args(args)
	print(args)
	try:
		imageTable.image2table(file_name=args.filename, outfile=args.output_file)

	except:
		raise

if __name__ == '__main__':
	main(sys.argv[1:])
