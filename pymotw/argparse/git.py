#coding:utf-8
import argparse

class InitAction(argparse.Action):
	'''根据命令创建目录'''
	def __call__(self, parser, namespace, values, option_string=None):
		import os
		path = values
		os.mkdir('./{}'.format(path))
		print '{} has been created'.format(path)

parser = argparse.ArgumentParser(prog="git", description="fake git tools written with python")

subparsers = parser.add_subparsers()

parser_init = subparsers.add_parser('init', help="init a directory", description="git initialize a dir.")
parser_init.add_argument('dir', action=InitAction)

parser_ls = subparsers.add_parser('ls', help="git list commands")

args = parser.parse_args()

parser.exit(0)