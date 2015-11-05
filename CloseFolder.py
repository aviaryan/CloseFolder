import sublime
import sublime_plugin
import os

class CloseFolder(sublime_plugin.TextCommand):
	'''
	CloseFolder class, closes files which belong to file's directory
	extends TextCommand class
	'''
	def run(self, edit):
		views = sublime.active_window().views()
		# use os.path.abspath
		dirname = os.path.dirname(self.view.file_name())
		for vw in views:
			if os.path.dirname(vw.file_name()) == dirname:
				vw.close()


class CloseFolderDirs(sublime_plugin.WindowCommand):
	'''
	CloseFolderDirs class, closes files from a directory, recursively
	'''
	def run(self, dirs=[]):
		views = sublime.active_window().views()
		for dr in dirs:
			dr += '\\'
			for vw in views:
				if (os.path.dirname(vw.file_name()) + '\\').find(dr) == 0:
					vw.close()