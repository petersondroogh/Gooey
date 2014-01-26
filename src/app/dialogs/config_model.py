'''
Created on Jan 23, 2014

@author: Chris
'''

import sys
import types
from model.source_parser import ArgumentError
from app.dialogs.action_sorter import ActionSorter



class Model(object):
	
	def __init__(self, parser):
		self._parser = parser 
		self.description = parser.description
		
		self.action_groups = ActionSorter(self._parser._actions)
		
		self._payload = None 
		

	def HasPositionals(self):
		if self.action_groups._positionals:
			return True
		return False
	
	def IsValidArgString(self, arg_string):
		if isinstance(self._Parse(arg_string), str):
			return False
		return True
	
	def _Parse(self, arg_string):
		try: 
			print self._parser.error
			self._parser.parse_args(arg_string.split())
			return True
		except ArgumentError as e:
			return str(e)
		
	def GetErrorMsg(self, arg_string):
		return self._FormatMsg(self._Parse(arg_string))
		
	def _FormatMsg(self, msg):
		output = list(msg)
		if ':' in output:
			output[output.index(':')] = ':\n '
		return ''.join(output)
	
	def AddToArgv(self, arg_string):
		sys.argv.extend(arg_string.split())
	


if __name__ == '__main__':
	pass
	
	
# 	print m2

	
	
	
